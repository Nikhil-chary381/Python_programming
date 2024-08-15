a={"bahubali","rrr","eega","shivam"}
for i in a:
    print(i)
print()
a.add(33)
a.add("ramam")
print("updated set:",a)
l=["hanuman","yamadonga"]
b={"og","tarak"}
a.update(l)
a.update(b)
print("after adding list and set to existing one:",a)
a.add("rrr")
print(a)
a.remove(33)
print(a)
a.pop()
print("result:",a)