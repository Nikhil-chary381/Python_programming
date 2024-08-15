n1=int(input("enter num1"))
n2=int(input("enter num2"))
s=0
try:
    s=n1/n2
except:
    print("division not possible")
else:
    print("result=",s)
finally:
    print("This is the code written in finally block")