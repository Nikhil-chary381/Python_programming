a=[1,8,2,4,3,1,2,3,10]
r=[]
print("list:",a)
for i in a:
    if i in r:
        pass
    else:
        r.append(i)
print("list after removal of duplicates:",r)