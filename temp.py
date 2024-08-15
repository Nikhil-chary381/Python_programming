n=int(input())
l1=[]
for i in range(0, n):
    e1=int(input())
    l1.append(set(map(int, input().split())))
    e2=int(input())
    l1.append(set(map(int, input().split())))
for i in l1[::2]:
    if l1.index(i)<len(l1)-1:
        j=l1.index(i)+1
        print(set(i).issubset(l1[j]))