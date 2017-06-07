##import turtle
##a=turtle.Turtle()
##n=8
##for i in range(n):
##    a.forward(70)
##    a.left(360/n)
##m=turtle.Turtle()
##m.shape("turtle")
##m.color("red")
##m.speed(3)
##m.penup()
##m.goto(-200,-50)
##m.pendown()
##delta=0.1*360/n
##for i in range(30):
##    m.forward(40+delta)
##    m.left(360/n+delta)
##    
class point:
    def __init__(self,col,xcoord=0,ycoord=0,):
        self.colour=col
        self.x=xcoord
        self.y=ycoord
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
    def get(self):
        return (self.x,self.y)
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
    def __rep__(self):
        return 'point('+str(self.x)+','+str(self.y)+')'

class card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def setRank(self,rank):
        self.rank=rank
    
