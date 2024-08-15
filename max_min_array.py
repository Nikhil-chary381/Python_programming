import array as arr
a=arr.array('i',[])
n=int(input("enter number of elements:"))
print("enter %d elements:"%n)
for i in range(n):
    a.append(int(input()))
print(a)
max=a[0]
min=a[0]
for i in a:print(i)
for i in a:
    if i>max:
        max=i
for i in a:
    if i<min:
        min=i
print("max element:",max)
print("min element:",min)