'''
Broadcasting is a powerful NumPy feature that pretends different sized arrays
or elements to have the same size so as to make some operations more efficient.
For instance, having:
x = np.array([1, 2, 3, 4])
y = 5

There's no way y can be added to x. However, there's a mechanism namely NumPy
that can shorten the path to perform the application so taht there's no need
to generate an array of 5's explictly then add it to the NumPy array. 
'''
