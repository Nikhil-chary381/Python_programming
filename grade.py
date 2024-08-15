n=int(input())
l1=[]
temp=[]
grade=[]
for i in range(0, n):
    l1.append(input())
    l1.append(float(input()))
    grade.append(l1[-1])
    temp.append(list(l1))
    l1.clear()
l=list(set(grade))
l.sort()
l.remove(l[0])
low2=min(l)
for i in temp:
    if low2 in i:
        l1.append(i[0])
    else:
        pass
l1.sort()
for i in l1:
    print(i)

    