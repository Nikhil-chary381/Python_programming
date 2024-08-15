with open("file3.txt", 'r') as rf, open("file1.txt", 'a') as wf:
    data=rf.readlines()
    for x in data:
        wf.write(x)