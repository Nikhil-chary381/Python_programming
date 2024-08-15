n=int(input("enter number of elements:"))
l=[]
print("enter %d numbers:"%n)
for i in range(n):
    l.append(int(input()))
print("our list: ",l)
l.sort()
print("list after sorting:",l)
print("maximum element in a list:",l[-1])
print("minimum element in a list:",l[0])
