class Rajamouli:
    def movie(self):
        print("student no 1")
class Keeravani:
    def music(self):
        print("MM keeravani")
class ntr(Rajamouli,Keeravani):
    def movies(self):
        print("student no1,simhadri,yamadonga,rrr")
obj=ntr()
obj.movie()
obj.music()
obj.movies()