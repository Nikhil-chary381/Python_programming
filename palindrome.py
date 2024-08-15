s=str(input("enter a string:"))
rev=s[::-1]
if s==rev:
    print(s," is a palindrome")
else:
    print(s," is not a palindrome")