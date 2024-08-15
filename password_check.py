print("********")
print("PASSWORD MUST CONTAIN ATLEAST ONE LETTER BETWEEN[a-z] AND BETWEEN[A-Z]")
print("ATLEAST 1 NUMBER BETWEEN[0-9]")
print("ATLEAST 1 CHARACTER FROM[$#@]")
print("MINIMUM LENGTH 6 CHARACTERS")
print("MAXIMUM LENGTH 16 CHARACTERS")
print("********")
p=input("enter your password:")
l=list(p)
if len(p) in range(6,17):
    if l.__contains__(range(ord('a'),ord('z')+1)) or l.__contains__(range(ord('A'),ord('Z')+1)) and range(0,10) in l and "$" in l or "@" in l or "#" in l:
        print("password is valid")

    else:
        print("enter valid password according to above specified characters")
elif len(p)<6:
    print("*minimum 6 characters required")
else:
    print("*only 16 characters")
