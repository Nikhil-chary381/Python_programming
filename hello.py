a=[]
n=int(input())
for i in range(0, n):
    a.append(int(input()))
a.sort()
a.remove(max(a))
print(max(a))