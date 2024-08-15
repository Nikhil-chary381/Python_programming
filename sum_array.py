import array as arr
n=int(input("enter number of elements:"))
a=arr.array('i',[])
print("enter %d elements :"%n)
for i in range(n):
    a.append(int(input()))
print("array is :",a)
sum=0
for i in a:
    sum+=i
print("sum of array elements: ",sum)