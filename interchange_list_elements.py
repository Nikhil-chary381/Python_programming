n=int(input("enter no of elements:"))
a=[]
for i in range(n):
    a.append(int(input()))
print("list:",a)
print("list after replacing 1st and last elements:")
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print(a)