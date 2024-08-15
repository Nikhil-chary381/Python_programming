import numpy
n=int(input("enter number of elements:"))
a=numpy.ndarray(shape=(n),dtype='i')
print("enter %d elements:"%n)
for i in range(n):
    a[i]=input()
print(a)
copy_array=a.copy()
view_array=a.view()
a[3]=20
print("copy array:",copy_array)
print("view of an array:",view_array)