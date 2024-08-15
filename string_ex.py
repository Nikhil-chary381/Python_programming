n=int(input("enter number of strings:"))
s=[]
count=0
index=0
print("enter elements:")
for i in range(0,n):
    s.append(input())
print(s)
for i in s:
    if len(i)>=2 and i[0]==i[-1]:
        count+=1
    else:
        pass
print("number of strings which has first and last characters equal: ",count)

