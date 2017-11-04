import math
###########################
#Question 1
###########################
def mh2kh(s):
    '''
    (number)->number
    Converts an mph value to kph.
    '''
    s = s*1.609344
    return s

###########################
#Question 2
###########################
def pythagorean_pair(a,b):
    '''
    (number,number)->boolean
    Returns true if math.sqrt(a**2+b**2) is an integer.
    '''
    c = math.sqrt(a**2+b**2)
    return c == int(c)

###########################
#Question 3
###########################
def in_out(xs,ys,side):
    '''
    (number,number,number)->none
    Prompts user to input coordinates, and prints True if the coordinates are within the square
    created by xs, ys, and side. The coordinates defined by xs and ys represent the lower left
    corner of the square.
    Preconditions: side must be positive.
    '''
    x = float(input('Enter a number for the x coordinate of a query point: '))
    y = float(input('Enter a number for the y coordinate of a query point: '))
    print(xs<=x<=(xs+side) and ys<=y<=(ys+side))
    
###########################
#Question 4
###########################
def safe(n):
    '''(int)->boolean
    Returns True if n is NOT divisible by 9 and does not contain 9 as a digit.
    Preconditions: n is a positive integer and is <100.
    '''
    n1=n//10
    n2=n%10
    return ((n1!=9 and n2!=9) and n%9!=0)
    
###########################
#Question 5
###########################
def quote_maker(quote,name,year):
    '''
    (string,string,int)->string
    Returns a sentence dispalying all three arguments.
    '''
    return ('In '+str(year)+' a person called '+name+' said: "'+quote+'"')


###########################
#Question 6
###########################
def quote_displayer():
    '''
    (none)->none
    Asks for user input on a quote, name, and year, and prints the return of quote_maker(quote,name,year)
    '''
    quote=input('Give me a quote: ')
    name=input('Who said that? ')
    year=input('What year did she/he say that? ')
    print(quote_maker(quote,name,year))

###########################
#Question 7
###########################
def rps_winner():
    '''
    (none)->none
    Plays rock-paper-scissors with two players.
    Preconditions: Player input is exactly one of the given options (case sensitive).
    '''
    p1=input('What choice did player 1 make?\nType one of the following options: rock, paper, scissors: ')
    p2=input('What choice did player 2 make?\nType one of the following options: rock, paper, scissors: ')
    print('Player 1 wins. That is '+str(((p1=='rock' and p2=='scissors') or (p1=='paper' and p2=='rock') or (p1=='scissors' and p2=='paper'))))
    print('It is a tie. That is not '+str(p1!=p2))
          
    
###########################
#Question 8
###########################
def fun(x):
    '''
    (number)->float
    Returns the y value for the equation 10**(4*y)==x+3.
    Precondition:x>0
    '''
    #The equation in terms of y is y=(ln(x+3))/((4)ln(10))
    return (math.log((x+3))/(4*math.log(10)))
    
###########################
#Question 9
###########################
def ascii_name_plaque(name):
    '''
    (str)->none
    Prints the name surrounded by a box of *
    '''
    print((10+len(name))*'*')
    print('*'+(8+len(name))*' '+'*')
    print('*  __'+name+'__  *')
    print('*'+(8+len(name))*' '+'*')
    print((10+len(name))*'*')
    
###########################
#Question 10
###########################
def draw_bike():
    '''
    (none)->none
    Draws a car with turtle graphics.
    '''
    #The link provided in a1-2017.pdf is a picture of a car, not a bike.
    s=turtle.Screen()
    t=turtle.Turtle()
    t.speed(0)
    t.goto(100,0)
    t.goto(-100,0)
    t.penup()
    t.goto(-150,-50)
    t.pendown()
    t.circle(50)
    t.penup()
    t.goto(150,-50)
    t.pendown()
    t.circle(50)
    t.penup()
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.left(180)
    t.forward(50)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(60)
    t.goto(-240,30)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(70)
    t.goto(270,30)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(70)
    t.penup()
    t.goto(-150,30)
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(-150,5)
    t.pendown()
    t.circle(5)
    t.right(90)
    t.forward(25)
    t.left(90)
    x1=0
    while x1!= 5:
        t.circle(30, 60)
        t.left(90)
        t.forward(25)
        t.left(180)
        t.forward(25)
        t.left(90)
        x1=x1+1
    t.setheading(180)
    t.penup()
    t.goto(150,30)
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(150,5)
    t.pendown()
    t.circle(5)
    t.right(90)
    t.forward(25)
    t.left(90)
    x1=0
    while x1!= 5:
        t.circle(30, 60)
        t.left(90)
        t.forward(25)
        t.left(180)
        t.forward(25)
        t.left(90)
        x1=x1+1
    t.setheading(90)
    t.penup()
    t.goto(-25,0)
    t.pendown()
    t.forward(175)
    t.left(180)
    t.goto(-120,175)
    t.goto(-170,90)
    t.penup()
    t.goto(-25,175)
    t.pendown()
    t.goto(70,175)
    t.goto(120,90)
    t.forward(50)
    t.penup()
    t.goto(-240,80)
    t.pendown()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(20)
    t.penup()
    t.goto(0,80)
    t.pendown()
    t.forward(15)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(240,70)
    t.shape("circle")
    t.shapesize(1,1.5,1)
    t.fillcolor("white")
    
    
###########################
#Question 11
###########################
def alogical(n):
    '''
    (number)->int
    Returns the minimum number of times that n must be divided by 2 in order to get a number equal to or smaller than 1.
    Preconditions: x>=1
    '''
    return math.ceil(math.log(n,2))
###########################
#Question 12
########################### 
def time_format(h,m):
    '''
    (int,int)->none
    Returns time in the format of a sentence.
    Preconditions: h and m are positive. 
    '''
    if 0>h or h>23:
        print('Invalid hour input.')
        return
    elif 0>m or m>59:
        print('Invalid minute input.')
        return
    m=5*round(m/5)
    if h==0:
        h='midnight'
    if (h=='midnight' and m==0):
        return('The time is '+h+'.')
    if m==0:
        return('The time is '+str(h)+" o'clock"+'.')
    elif m==30:
        return('The time is half past '+str(h)+'.')
    elif m==60:
        if h+1==24:
            return('The time is midnight.')
        else:
            return('The time is '+str(h+1)+" o'clock"+'.')
    elif m>30:
        if h+1==24:
            h='midnight'
            return('The time is '+str(60-m)+' minutes to '+str(h)+'.')  
        else:
            return('The time is '+str(60-m)+' minutes to '+str(h+1)+'.')
    else:
        return('The time is '+str(m)+' minutes past '+str(h)+'.')
    #O'clock is not commonly used except when referring to m==0, so it was purposefully omitted in all other cases.
    #Added midnight clause to avoid 'The time is 0.' statements. 

    
###########################
#Question 13
###########################
def cad_cashier(price,payment):
    '''
    (number,number)->number
    Returns change rounded to the nearest 0.05
    Preconditions: payment>=price, payment's second decimal is 0 or 5
    '''
    change = round(0.05*round((payment-price)/0.05),2)
    #The outer round function is called to eliminate python's float inacuracy.
    return change
        
###########################
#Question 14
###########################
def min_CAD_coins(price,payment):
    '''
    (number,number)->8 numbers
    Returns change in coins, excluding pennies.
    Preconditions: payment>=price, payment's second decimal is 0 or 5
    '''
    change = cad_cashier(price,payment)
    t=change//2
    change=change%2
    l=change//1
    change=change%1
    q=change//0.25
    change=change%0.25
    d=change//0.10
    change=change%0.10
    n=round((change/0.05),2)
    #The round function is called to eliminate python's float inacuracy.
    return (t,l,q,d,n)

def min_enclosing_rectangle(radius,x,y):
    '''
    (number,number,number)->(number,number) or None
    Gives lower left coordinate of a rectangle with minimal area that encompasses a circle defined by
    radius, x, and y (origin coordinates).
    Precondition: radius<0
    '''
    if radius<0:
        return None
    cxl=x-radius
    cyb=y-radius
    return(cxl,cyb)


def series_sum():
    '''
    (none)->number
    Prompts user for input n and returns 1000+sigma[1,n][1/n^2].
    '''
    n=int(input('Please enter a non-negative integer: '))
    if n<0:
        return None
    else:
        i=1
        sum=1000
        while i<n+1:
            sum=sum+(1/(i**2))
            i=i+1
        return sum

    
def pell(n):
    '''
    (int)->int or None
    Returns nth Pell number.
    Precondition: n>=0
    '''
    if n<0:
        return None
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(2*pell(n-1)+pell(n-2))

    
def countMembers(s):
    '''
    (str)->int
    returns number of special characters in s.
    '''
    list=['e','f','g','h','i','j','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','2','3','4','5','6','!',',','\\']
    tally=0
    for i in s:
        if i in list:
            tally=tally+1
    return tally


def casual_number(s):
    '''
    (str)->int
    Removes commas from numbers.
    '''
    try:
        return int(s.replace(',',''))
    except ValueError:
        return None

    
def alienNumbers(s):
    '''
    (str)->int
    Translates alien symbol sequences into numbers.
    Preconditions: s is comprised only of alien symbols.
    '''
    list=[]
    for i in s:
        list.append(i)
    for idx, i in enumerate(list):
        if list[idx]=='T':
            list[idx]=1024
        if list[idx]=='y':
            list[idx]=598
        if list[idx]=='!':
            list[idx]=121
        if list[idx]=='a':
            list[idx]=42
        if list[idx]=='N':
            list[idx]=6
        if list[idx]=='U':
            list[idx]=1
    return sum(list)


def alienNumbersAgain(s):
    '''
    (str)->int
    Translates alien symbol sequences into numbers.
    Preconditions: s is comprised only of alien symbols.
    '''
    #Code is the same as before because no string methods were used to begin with.
    list=[]
    for i in s:
        list.append(i)
    for idx, i in enumerate(list):
        if list[idx]=='T':
            list[idx]=1024
        if list[idx]=='y':
            list[idx]=598
        if list[idx]=='!':
            list[idx]=121
        if list[idx]=='a':
            list[idx]=42
        if list[idx]=='N':
            list[idx]=6
        if list[idx]=='U':
            list[idx]=1
    return sum(list)
