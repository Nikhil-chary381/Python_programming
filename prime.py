n=int(input("enter number:"))
a=[]
for i in range(1,n):
    if i==1:
        a.append(i)
    elif n%i==0:
        a.append(i)
    else:
        pass
print(len(a))
if len(a)==1 and a[0]==1:
    print(n," is a prime number")
else:
    print(n," is not a prime number")
        
