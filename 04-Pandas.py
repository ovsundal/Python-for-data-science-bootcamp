import numpy as np
import pandas as pd

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

