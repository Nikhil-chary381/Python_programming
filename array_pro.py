import array as arr
n=int(input("enter size of array:"))
a=arr.array('i',[])
print("enter %d elements:"%n)
for i in range(0,n):
    e=int(input())
    a.append(e)
print("entered numbers are:",a)
for i in range(0,n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("after sorting:")
print(a)
#removing elements from the array
#a.remove(2)
print(a.pop(2))
print("array after deleting 2nd index number")
print(a)
