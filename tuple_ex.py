l1=[(2,3),(1,2),(6,4),(4,1)]
t=dict(l1)
temp=[]
l2=list(t.values())
print(l2)
l2.sort()
print(l2)
for i in l2:
    a=tuple(t.