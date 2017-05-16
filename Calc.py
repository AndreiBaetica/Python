






import operator
import functools


op1=input("Choose one of three functions: a) Multiplication, b) Addition, c) Division: ")
while not (op1=='a' or op1=='b' or op1=='c'):
    print("Invalid input. Type only the lowercase letter corresponding with the desired operation.")
    op1=input("Choose one of three functions: a) Multiplication, b) Addition, c) Division: ")
if op1=='a':
    fac1=input("State how many factors you wish to multiply: ")
    try:
        int(fac1)
    except:
        ValueError or fac1=='1'
        print("Invalid input.")
        fac1=input("State how many factors you wish to multiply: ")
        int(fac1)
    f1=float(input("Enter the first factor: "))
    multlist=[f1]
    multinput=0
    while multinput<int(fac1)-1:
        multlist.append(float(input("Enter the next factor: ")))
        multinput=multinput+1
    multanswer=functools.reduce(operator.mul,multlist,1)
    print("The product is:",str(multanswer)+".")
