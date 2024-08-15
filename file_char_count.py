a=input("enter file name:")
f=open(a,'r')
lines=0
char=0
words=0
x=f.read()
for i in x:
    if i=='\n':
        lines+=1
    else:
        char+=1

