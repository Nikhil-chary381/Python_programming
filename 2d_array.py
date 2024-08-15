import numpy
m=int(input("enter number of rows:"))
n=int(input("enter number of columns:"))
a=numpy.ndarray(shape=(m,n),dtype=int)
print("enter %d elements :"%(m*n))
for i in range(m):
    for j in range(n):
        a[i][j]=int(input())
print("numpy array is:")
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)
print(len(a[0]))