a=("hello","nikhil","vinay")
print(a)
print()
for i in a:
    print(i)
print()
b=list(a)
b.append(22)
b.append("ram")
print("tuple after updated by transforming into list:")
c=tuple(b)
print(c)
b=list(c)
b.extend([66,"oop"])
b.remove(22)
a=tuple(b)
print("result:",a)

