import numpy
r1=int(input("enter rows of matrix A:"))
c1=int(input("enter columns of matrix A:"))
a=numpy.ndarray(shape=(r1,c1),dtype='i')
print("enter %d elements of matrix:"%(r1*c1))
for i in range(r1):
    for j in range(c1):
        a[i][j]=int(input())
r2=int(input("enter rows of matrix B:"))
c2=int(input("enter columns of matrix B:"))
b=numpy.ndarray(shape=(r2,c2),dtype='i')
print("enter %d elements of matrix:"%(r2*c2))
for i in range(r2):
    for j in range(c2):
        b[i][j]=int(input())
c=numpy.ndarray(shape=(c1,r2),dtype='i')
#c[0][0]=0
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print("Multiplication of 2 matrices:")
print(c)
