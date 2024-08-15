class Add:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c=0):
        return a+b+c
obj=Add()
print(obj.sum(2,1))
print(obj.sum(2,1,3))