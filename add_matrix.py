import numpy
r=int(input("enter rows:"))
c=int(input("enter columns:"))
a=numpy.ndarray(shape=(r,c),dtype='i')
print("enter %d elements of matrix:"%(r*c))
for i in range(r):
    for j in range(c):
        a[i][j]=int(input())
b=numpy.ndarray(shape=(r,c),dtype='i')
print("enter %d elements of matrix:"%(r*c))
for i in range(r):
    for j in range(c):
        b[i][j]=int(input())
c=numpy.ndarray(shape=(r,c),dtype='i')
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
print("sum of matrices A and B:")
print(c)