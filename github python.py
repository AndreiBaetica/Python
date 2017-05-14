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


#Counts the values in a string.
def count_vowels(string):
    '''(str)->int'''
    counter=0
    for x in string:
        if x in 'aeiouAEIOU':
            counter=counter+1
    return counter
