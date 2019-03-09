import numpy as np

my_list = [1, 2, 3]

# return evenly spaced values within a given interval (start, end, step)
print(np.arange(0, 10, 2))

# return zero / one (use ones) matrix (num_rows, num_cols)
print(np.zeros((2, 2)))

# return evenly spaced numbers between two values (min, max, num values)
print(np.linspace(0, 5, 15))

# return Identity matrix
print(np.eye(4))

# return randomly populated array (0-1)
print(np.random.rand(5, 5))

# return randomly populated array from normal distribution
print(np.random.randn(2))

# return randomly populated array from min (inc) - max (exc)
print(np.random.randint(1, 100, 10))

# populate random array
ranarr = np.random.randint(0, 50, 10)
print(ranarr)

# find highest/lowest value in array
print(ranarr.max())
print(ranarr.min())

# find index location of highest/lowest value in array
print(ranarr.argmax())
print(ranarr.argmin())

# reshape a matrix, keeping values
print(ranarr.reshape(10))
print(ranarr.reshape(5, 2))

arr = np.arange(0, 11)
print(arr)
# slice an array, min (inc) to max (exc)
print(arr[1:5])

# set first 5 indexes equal to 100
arr[0:5] = 100
print(arr)

# create subarray (with value references)
slice_of_arr = arr[0:6]
slice_of_arr[:1] = 100
print(slice_of_arr)

# create new array (copy data values)
arr_copy = arr.copy()
arr_copy[0:2] = 50
print(arr_copy)

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
# access [row][column] of matrix
print(arr_2d[0][2])

# access sections of matrix (grab everything excluding row 2, with all elements from index 1)
print(arr_2d[:2, 1:])

# predicate comparison for all array indexes
arr = np.arange(1, 11)
bool_arr = arr > 5
print(bool_arr)

# only get results where bool_arr evaluates to true (conditional selection)
print(arr[bool_arr])

# get all results where arr is greater than 3
print(arr[arr > 3])

arr = np.arange(0, 11)
# add constant to all indexes
print(arr + 100)

# square root of all elements in array
print(np.sqrt(arr))

# EXERCISES

# Create an array of 10 zeroes
print(np.zeros(10))

# Create an array of 10 ones
print(np.ones(10))

# Create an array of 10 fives
print(np.zeros(10) + 5)

# Create an array of the integers from 10 to 50
print(np.arange(10, 51, 2))

# Create a 3x3 matrix with values ranging from 0 to 8
print(np.arange(0, 9).reshape(3, 3))

# Create a 3x3 identity matrix
print(np.identity(3))

# Use NumPy to generate a random number between 0 and 1
print(np.random.rand(1))

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.rand(25))

# Create this matrix
print(np.arange(0.01, 1.01, .01).reshape(10, 10))

# Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0, 1, 20))

# Grab a chunk from this matrix
mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print(mat[2:, 1:])
print(mat[3][4])
print(mat[:3, [1]])
print(mat[4])
print(mat[3:])

# Get sum of all values in matrix
print(np.sum(mat))

# Get standard deviation
print(np.std(mat))

# Get the sum of all the columns in mat
print(np.sum(mat, 0))
