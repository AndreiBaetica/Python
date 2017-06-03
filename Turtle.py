import turtle
a=turtle.Turtle()
n=8
for i in range(n):
    a.forward(70)
    a.left(360/n)
m=turtle.Turtle()
m.shape("turtle")
m.color("red")
m.speed(3)
m.penup()
m.goto(-200,-50)
m.pendown()
delta=0.1*360/n
for i in range(30):
    m.forward(40+delta)
    m.left(360/n+delta)
    
