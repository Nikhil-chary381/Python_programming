l=[]
c=0
for i in range(100,401):
    s=str(i)
    for j in s:
        if int(j)%2==0:
            c=1
        else:
            c=0
            break
    if c==1:
        l.append(i)

print(l)
        