#Quadratic Equation Solver
import math
def qe_solver(a,b,c):
    '''(number,number,number)->None'''
    if a==0:
        if b!=0:
            print("The linear equation",str(b)+"x+"+str(c)+"=0")
            print("has the following root:", -c/b)
        else:
            if c==0:
                print("The equation is always true")
            else:
                print("The equation has no solution")
    else:
        discr=b**2-4*a*c
        if discr>=0:
            x1=(-b+math.sqrt(discr))/(2*a)
            x2=(-b-math.sqrt(discr))/(2*a)
            print("The quadratic equation", str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0")
            print("Has the following two roots:", str(x1)+","+str(x2))

        else:
            print("The quadratic equation", str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0")
            print("has the following two complex roots: ")
            print(str(-b/(2*a))+"+i"+str(math.sqrt(abs(discr))/(2*a)),"and")
            print(str(-b/(2*a))+"-i"+str(math.sqrt(abs(discr))/(2*a)),"and")

print("Welcome to the quadratic equation solver.")
a1=float (input("Enter a number for the coefficient a: "))
b1=float (input("Enter a number for the coefficient b: "))
c1=float (input("Enter a number for the coefficient c: "))

qe_solver(a1,b1,c1)


#Prints a word in a column. Letters separated by stars.  
def column_stars(word):
    '''(str)->None'''
    for a in word:
        print(a)
        print("***")


#Counts the vowels in a string.
def count_vowels(string):
    '''(str)->int'''
    counter=0
    for x in string:
        if x in 'aeiouAEIOU':
            counter=counter+1
    return counter


#Removes all non-vowel characters in a string.
def only_vowels(string):
    '''(str)->str'''
    vowels=''
    for a in string:
        if a in 'aeiouAEIOU':
            vowels=vowels+a
    return vowels


#Prints x number of rectangles.
def rectangles(x):
    '''(int)->none'''
    for i in range(x):
        print('********')
        print('*      *')
        print('*      *')
        print('*      *')
        print('*      *')
        print('*      *')
        print('********')


#Counts to x.
def counter(x):
    '''(int)->none'''
    for i in range(x):
        print(i+1)


#Prints even numbers only.
def even_only(x):
	'''(int)->none'''
	for i in range(x):
		if i%2==0:
			print(i)

#Generates a Fibonnaci sequence up to a given number.
def fibonnaci_sequence():
    '''(None)->list'''
    n=int(input("State how many Fibonnaci sequence numbers to generate: "))
    y=1
    if n==0:
        f=[]
    elif n==1:
        f=[1]
    elif n==2:
        f=[1,1]
    elif n>2:
        f=[1,1]
        while y<(n-1):
            f.append(f[y]+f[y-1])
            y+=1
        return f

#Generates two random lists of 100 integers, and prints only the numbers found in both.
import random

def duplicateChecker():
    '''(none)->lst'''
    lst1=[]
    lst2=[]
    for a in range(0,99):
        a=random.randint(1,100)
        lst1.append(a)
    for b in range(0,99):
        b=random.randint(1,100)
        lst2.append(b)
    result=[]
    for x in lst1:
        if x in lst2:
            result.append(x)
    print(set(result))

#Generates a 10 character long random password.
import random
def passwordGenerator():
    '''(None)->None'''
    password='!@#$%^&*()_+1234567890-=QWERTYUIOP{}|qwertyuiop[]\ASDFGHJKL:asdfghjkl;ZXCVBNM<>?zxcvbnm,./'
    r=random.sample(password,10)
    Input=""
    while Input!="exit":
        Input=input("Press enter to generate new password or type exit to exit ")
        if Input =="":
            r=random.sample(password,10)
            r="".join(r)
            print (r)
        elif Input =="exit" or "Exit":
            break
            exit()

#Checks if a number is prime.
def prime():
    '''(int)->none'''
    x=int(input("Enter a number: "))
    div=[]
    for y in range(1,x+1):
        if x%y==0:
            div.append(y)        
    if len(div)==2:
        print("Prime.")
    else:
        print("Not prime.")

#Plays rock-paper-scissors against the CPU
import random
def rps():
    '''(None)->None'''
    u=input("R/P/S? ")
    q=["R","P","S"]
    c=random.choice(q)
    print("CPU's choice:"+c)
    if u=="R":
        if c=="R":
            print("Draw")
        elif c=="P":
            print("Defeat")
        elif c=="S":
            print("Victory")
    elif u=="P":
        if c=="R":
            print("Victory")
        elif c=="P":
            print("Draw")
        elif c=="S":
            print("Defeat")
    elif u=="S":
        if c=="R":
            print("Defeat")
        elif c=="P":
            print("Victory")
        elif c=="S":
            print("Draw")
    
