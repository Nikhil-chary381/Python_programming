n=int(input("enter no of elements:"))
a=[]
for i in range(n):
    a.append(int(input()))
print("list:",a)
pos1=int(input("enter pos1:"))
pos2=int(input("enter pos2:"))
temp=a[pos1-1]
a[pos1-1]=a[pos2-1]
a[pos2-1]=temp
print("after replacement:")
print(a)