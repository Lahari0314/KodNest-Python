class Rectangle:
    def __init__(self,len,wid):
        self.l=len
        self.w=wid

    def area(self):
        return self.l*self.w

class Square:
    def __init__(self,side):
        self.s=side
    def area(self):
        return self.s*self.s

len=int(input())
wid=int(input())
side=int(input())
print(Rectangle(len,wid).area())
print(Square(side).area())