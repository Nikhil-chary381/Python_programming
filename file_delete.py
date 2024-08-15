import os
a=os.remove("file1.txt")
if a:
    print("successfully file deleted")
else:
    print("something went wrong")