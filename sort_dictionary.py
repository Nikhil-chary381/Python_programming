a={10:"ten",2:"two",3:"three",5:"five"}
new=dict()
l1=list(a.keys())
l1.sort()
for i in l1:
    new[i]=a.get(i)
print(new)