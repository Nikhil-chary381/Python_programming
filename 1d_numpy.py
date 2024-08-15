import numpy
n=int(input("enter size of list:"))
a=numpy.ndarray(shape=(n),dtype=int)
print("enter elements:")
for i in range(0,n):
    a[i]=input()
print("numpy array:",a)
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)
