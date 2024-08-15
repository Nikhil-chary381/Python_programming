n=int(input())
a=input()
l1=a.split()
l2=[]
for i in l1:
    l2.append(int(i))
s=set(l2)
l=list(s)
l.sort()
print(l)
l.remove(max(l))
print(max(l))
