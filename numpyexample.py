import numpy as np

# a = np.array([[1,2,3], 
#               [4,5,6]
#               ])

# print(a.shape)

# a = np.array([1,2,3,4,5,6])
# print(a)

# print(a[0])

# a[0] = 10
# print(a)

# # slice Notation
# # slicing the array uses the view function meaning the original array is changed
# print(a[:3])
# b = a[3:]
# print(b)
# b[0] = 40
# print(a)

# c = np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,10,11,12]])

# print(c.shape) # shape of an array
# print(c.ndim) # number of dimensions of an array
# print(c[0,3])
# print(c.size) # number of elements in an array

# # CREATING BASIC ARRAYS
# t = np.zeros([8,5, 2])
# print(t.size)

# y = np.empty([2,5]) # create an empty array with random values
# print(y)

# # arange = create an array with a range of values
# h = np.arange(3, 9, 1) # first number, last number and step size
# print(h)

# # linspace is to create an array with values spaced linearly 
# print(np.linspace(0, 10, num=5))

# print(h.dtype)

# x = np.ones(3, dtype=np.float64)
# print(x.dtype)

# # ADDING REMOVING AND SORTING ELEMENTS
# array = np.array([2,1,5,3,7,4,6,8])
# print(np.sort(array))

# print(np.argsort(array, axis=-1, kind='mergesort')) # argsort is an indirect sort along a specific axis

# # concatenating elements
# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# print(np.concatenate((a,b)))

# # RESHAPING AN ARRAY
# # with reshaping, do it such that the multiple will give you the total elements in the original array rows x columns
# q = np.arange(10)
# print(q)

# w = q.reshape(2,5)
# print(w)

# q = np.arange(10)
# print(np.reshape(q, shape=(1,10), order='C'))

# a = np.array([1,2,3,4,5,6])
# print(a.shape)

# a2 = a[np.newaxis, :] # newaxis increases the dimension of the array by 1, 1D->2D, 2D->3D, this is for row axis
# print(a2.shape)

# a2 = a[:, np.newaxis] # this create a new dimension along the columns
# print(a2.shape)

# e = np.array([1,2,3,4,5,6])
# print(e.shape)

# g = np.expand_dims(e, axis=1)
# print(g.shape)

# a = np.array([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])
# print(a[a < 5])

# five_up = a[a >= 5]
# print(five_up)

# five_up = (a > 5) | (a == 5) # or condition(|) returns a bool of the array that submit to it
# print(five_up)

# b = np.nonzero(a < 5) # returns array of rows where the condition is met, second array return the columns where condition is met
# print(b)

# loc = list(zip(b[0], b[1]))
# for coord in loc:
#     print(coord)