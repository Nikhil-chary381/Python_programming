class Hello:
    x=10
    print("Hello world")
    def __init__(self):
        print("init method in python")
    def display(self):
        print("display method")
o=Hello()
print(o.x)
o.display()