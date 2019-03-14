import numpy as np
import pandas as pd

from numpy.random import randn

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

# Create a series from string and number array
print(pd.Series(my_data, labels))

# Create a series from np
print(pd.Series(arr, labels))

# Create a series from dictionary
print(pd.Series(d))

# Create a series with built-in functions
print(pd.Series([sum, print, len]))

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
ser3 = pd.Series(labels)

# Sum together series with equal keys
print(ser1 + ser2)

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

# Grab columns from DataFrame using bracket notation
print(df['W'])
# DataFrame is just a collection of Series
print(type(df['W']))
# Pass in a list in order to grab several columns
print(df[['W', 'Z']])

df['new'] = df['W'] + df['Y']
print(df['new'])

# Drop a row (rows referred to as 0-axis, columns as 1-axis) inplace=True means permanently drop
df.drop('E', axis=0, inplace=False)
print(df)

# Get row/columns of matrix
print(df.shape)

# Select rows from dataframe (as series)
print(df.loc['A'])

# Select rows (index based location)
print(df.iloc[2])

# Select cell from (row, col)
print(df.loc['B', 'Y'])

# Select multiple cells
print(df.loc[['A', 'B'], ['W', 'Y']])

# Conditional selection (get all cell values relative to predicate)
print(df > 0)
print(df[df > 0])

# Return bool values of col W
print(df['W'] > 0)
# Only return true values of col W
print(df[df['W'] > 0])

# Grab all rows in dataframe where Sum(row) < 0
print(df[df['Z'] < 0])

resultdf = df[df['W'] > 0][['X', 'Y']]
print(resultdf)

# Multiple conditions (use ampersand instead of and when dealing with a series of bool values)
print(df[(df['W'] > 0) & (df['Y'] > 1)])

# Reset index (only here)
print(df.reset_index(inplace=False))

new_ind = 'CA NY WY OR CO'.split()
print(new_ind)

# Add new column
df['States'] = new_ind
print(df)

# Set new index
print(df.set_index('States'))

# Index hierarchy
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])

print(df)
print(df.loc['G1'])
print(df.loc['G1'].iloc[1])

# Set label indexes
df.index.names = ['Groups', 'Num']
print(df)

print(df.loc['G2'].loc[2]['B'])

# Cross section grab
print(df.xs(1, level='Num'))

# Missing data
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)

# Drop all rows with null/NaN values
print(df.dropna())

# Drop all columns with null/NaN values
print(df.dropna(axis=1))

# Drop rows with x null/NaN values
print(df.dropna(thresh=2))

# Fill null/NaN values
print(df.fillna(value='FILL'))

# Group by with aggregate functions
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)
groupByComp = df.groupby('Company')
# group by mean value (ignores string columns)
print(groupByComp.mean())

print(groupByComp.sum().loc['FB'])
print(groupByComp.count())
print(groupByComp.min())
print(groupByComp.describe().transpose())

# Operations
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

print(df.head())
# Find unique values in dataframe (nunique for counting)
print(df['col2'].unique())

print(df['col2'].value_counts())

# Conditional selection
print(df[(df['col1'] > 2) & (df['col2'] == 444)])


def times2(x):
    return x * 2


print(df['col1'])
# Apply custom function
print(df['col1'].apply(times2))
print(df['col1'].apply(lambda x: x * 2))

# Remove columns
print(df.drop('col1', axis=1))

# Sort by column 2
print(df.sort_values('col2'))

# Find null values
print(df.isnull())

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)

print(df)
# Create pivot table
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))
