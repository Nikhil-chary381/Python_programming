with open("file3.txt",'r') as f:
    n=[]
    result=[]
    s=f.read()
    a=s.split("\n")
    for i in a:
        n.extend(i.split(" "))
    for j in n:
        result.extend(j.split(","))
    print(result)
    print("number of words in a file: ",len(result))
