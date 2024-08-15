n1=input("enter value1:")
n2=input("enter value2:")
try:
    if type(n1) is int and type(n2) is int:
        sum=n1+n2
        print("sum of 2 numbers is:",sum)
    else:
        raise Exception
except Exception as e:
    print(e,"type of 2 values must be same")