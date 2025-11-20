import numpy as np


array = np.array([
    [1, 2, 4],
    [1, 2, 4],
    [1, 2, 4],
])

'''
    array transforms sequences of sequences into two-dimensional arrays, sequences of sequences 
    of sequences into three-dimensional arrays, and so on
'''
array2 = np.array((
    [
        [2, 3, 2, 3],
        [2, 3, 2, 3]
    ],
    [
        [2, 3, 2, 3],
        [2, 3, 2, 3]
    ],
    [
        [2, 3, 2, 3],
        [2, 3, 2, 3]
    ]
))

# Explicitly specifying type of array
array3 = np.array([1, 4, 5], dtype=complex)

# Number of axes/dimensions
# print("Number of dimensions: ", array.ndim)

# Size of the array in each dimension
# print("Size in each dimension: ", array2.shape)

# Total number of elements in the array
# print("Size: all ", array.size)

# Type of arry - deduced from the elements in the array
# print("Type: ", array.dtype)


# Numpy offers several functions to create arrays with placeholder content

# ZEROS - creates an array full of zeros - takes in a tuple as the argument to define the shape
array5 = np.zeros((2, 3))
# print(array5)

# ONES - creates an array full of ones
array6 = np.ones((2, 2, 4))
# print(array6)

# EMPTY - creates an array with random elements
array7 = np.empty((3, 3))
# print(array7)

# ARANGE - analogous to the python built-in range function, but returns an array
# it takes in start and optional stop and step as argument
array8 = np.arange(0, 10)
array9 = np.arange(0, 10, 2)

# Not possible to predict the number of elements because of floating point used as step
array10 = np.arange(0, 5, 0.3)
# print(array8)


''' LINSPACE - function like "arange" but the third argument is the number of element that 
we want to be within the range, instead of step '''
array11 = np.linspace(0, 5, 10)
# By default the number of elements is 50 to be generated is 50
array12 = np.linspace(0, 5, 4)
# print(array12)


# BASIC OPERATIONS
# Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.
a = np.array([4, 1, 3, 3])
b = np.array([2, 1, 4, 1])

# ADDITION AND SUBTRACTION
c = a - b    # doesn't change the array in "a"
c1 = np.ones((4))
c2 = c + c1
# print(c)
# print(c2)

# MULTIPLICATION
array44 = np.array([
    [2, 6],
    [3, 4]
])
# print(array44 * 2)

# Division
array45 = array44 / 10
# print(array45)


''' The matrix product can be performed using the @ operator (in python >=3.5) or the 
dot function or method '''

# MATRIC PRODUCT
x = np.array([
    [1, 2],
    [3, 4]
])

y = np.array([
    [2, 4],
    [1, 3]
])

# print(x @ y)
# print(y.dot(x))

''' Some operations, such as += and *=, act in place to modify an existing array rather 
than create a new one. '''
array110 = np.ones((2, 4), dtype=int)
array110 *= 3
# print(array110)


# default_rng - Creates an instance of the random generator
''' When you pass the same seed (e.g., 1), the generator will always produce the same 
sequence of random numbers '''
rg = np.random.default_rng(1) 
rg2 = np.random.default_rng() # generate a unique sequence everytime 
rand1 = rg.random((2, 3))
rand2 = rg2.random((2, 3))
# print(rand1)
# print(rand2)


''' Many unary operations, such as computing the sum of all the elements in the array, 
are implemented as methods of the ndarray class '''
array200 = rg.random((2, 3))

# print(array200)
# sum
# print(array200.sum())
# min
# print("min", array200.min())
# max
# print("max", array200.max())

''' By default, these operations apply to the array as though it were a list of numbers, 
regardless of its shape. However, by specifying the axis parameter you can apply an operation
along the specified axis of an array'''
array22 = np.array([
    [ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11]
])

# print(array22.sum(axis=0)) # Sum of each column
# print(array22.min(axis=0)) # Min of each column

# print(array22.sum(axis=1)) # Sum of each row
# print(array22.min(axis=1)) # Min of each row


# INDEXING, SLICING AND ITERATION

# slicing of one-dimensional array
array_xyz = np.arange(10) ** 2
# print(array_xyz[5])
# print(array_xyz[0: 4])

# From start 0 to finish 6, set every second element to 1000
array_xyz[0:6:2] = 1000
# print(array_xyz)
# print(array_xyz[::-1]) # reverse the array

# multi-dimensional array
array_z = np.array([
        [ 0,  1,  2,  3],
        [10, 11, 12, 13],
        [20, 21, 22, 23],
        [30, 31, 32, 33],
        [40, 41, 42, 43]])

# print(array_z[2, 3]) # 23
# print(array_z[0:3, 3]) # 4th column of the first three rows
# print(array_z[:, 1]) # second column of each row
# print(array_z[1:3, :]) # Each column in the second and third row

''' When fewer indices are provided than the number of axes, the missing 
indices are considered complete slices : '''

# print(array_z[-1]) # is equivalent to array_z[-1, :]

''' Using ... to represent as many colons as needed to produce a complete indexing tuple
    Example, if x is an array with 5 axes
    x[1, 2, ...] is equivalent to x[1, 2, :, :, :]
    x[..., 3] to x[:, :, :, :, 3]
    x[4, ..., 5, :] to x[4, :, :, 5, :]
'''

# print(array_z[..., 0:3])


# Iterating over multi-dimensional array is done with respect to the first axis
for row in array_z:
    print(row)

# Perform operation on each element of the array using the flat attribute
for elemnt in array_z.flat:
    print(elemnt)
