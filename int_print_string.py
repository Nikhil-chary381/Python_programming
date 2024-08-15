d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
n=int(input("enter number:"))
s=str(n)
temp=""
c=d.keys()
for i in s:
    if int(i) in c:
            temp+=d.get(int(i))
            temp+='-' 
print(temp[:len(temp)-1])
