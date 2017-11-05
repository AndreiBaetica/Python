import math
import random
def primary_school_quiz(flag, n):
    '''
    (int,int)->int
    Generates an n question long quiz on either subtraction or exponentiation. If flag is 0, subtraction is used.
    If flag is 1, exponentiation is used. Returns the number of correct answers.
    Preconditions: flag==1 or flag==0
    '''
    score=0
    q=1
    if flag==0:
        while q!=n+1:
            a=random.randint(0,9)
            b=random.randint(0,9)
            ans=int(input("Question "+str(q)+':\nWhat is the result of '+str(a)+'-'+str(b)+'?'))
            if ans==(a-b):
                score=score+1
            q=q+1
    else:
        while q!=n+1:
            a=random.randint(0,9)
            b=random.randint(0,9)
            ans=int(input("Question "+str(q)+':\nWhat is the result of '+str(a)+'^'+str(b)+'?'))
            if ans==(a**b):
                score=score+1
            q=q+1
    return (score/n)*100

def high_school_eqsolver(a,b,c):
    #TODO: Finish
    '''
    (number,number,number)->none
    returns roots of a quadratic formula with coefficients a, b, and c.
    '''
    pass



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

ascii_name_plaque('Welcome to my math quiz-generator / equation-solver')

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    ascii_name_plaque(name+', welcome to my quiz-generator for primary school students.')
    flag=int(input("What would you like to practice? Enter\n0 for subtraction\n1 for exponentiation"))
    n=int(input("How many practice questions would you like to do?"))
    score=primary_school_quiz(flag, n)
    if score>=90:
        print('Congratulations '+name+'! You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep.')
    elif (score>=70 and score<90):
        print('You did well '+name+', but I know you can do better.')
    else:
        print('I think you need some more practice '+name+'.')
        
elif status=='2':
    ascii_name_plaque('quadratic equation, ax^2+bx+c=0 solver for '+name)
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")
        question.strip().lower()
        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a=float(input('Enter a number the coefficient a: '))
            b=float(input('Enter a number the coefficient b: '))
            c=float(input('Enter a number the coefficient c: '))        
            high_school_eqsolver(a,b,c)
else:
    print(name+' you are not a target audience for this software.')
    
print("Good bye "+name+"!")


