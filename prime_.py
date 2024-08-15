n=int(input("enter number"))
l1=[]
for i in range(2,n):
    if n%i==0:
        l1.append(i)
    else:
        pass
if len(l1)==0:
    print(n," is a prime number")
else:
    print(n," is not a prime number")