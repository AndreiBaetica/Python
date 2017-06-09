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
    def __repr__(self):
        return 'Card('+str(self.rank)+','+str(self.suit)+')'
    def __eq__(self,other):
        if self.rank==other.rank and self.suit==other.suit:
            return True
        else:
            return False

import random
class deck:
    ranks={'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    suits={'\u2660','\u2661','\u2662','\u2663'}
    def __init__(self):
        self.deck=[]
        for rank in deck.ranks:
            for suit in deck.suits:
                self.deck.append(Card(rank,suit))
    def shuffle(self):
        random.shuffle(self.deck)
    def dealCard(self):
        return self.deck.pop()
    def __len__(self):
        return len(self.deck)

class animal:
    def __init__(self,species,language):
        self.spec=species
        self.lang=language
        def get(self):
            return(self.spec,self.lang)
        def speak(self):
            print('I am a',self.spec,'and I',self.lang)

class birb(animal):
    def __init__(bl,self,species,language):
        self.bl=bl
        super().__init(species,language)
    def speak(self):
        print(3*self.lang)
    def get(self):
        print(self.bl,end=' ')
        super().get()

