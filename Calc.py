






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
elif op1=='b':
    add1=input("State how many numbers you wish to add: ")
    try:
        int(add1)
    except:
        ValueError or add1=='1'
        print("Invalid input.")
        add1=input("State how many factors you wish to multiply: ")
        int(add1)
    a1=float(input("Enter the first number: "))
    addlist=[a1]
    addinput=0
    while addinput<int(add1)-1:
        addlist.append(float(input("Enter the next factor: ")))
        addinput=addinput+1
    addanswer=sum(addlist)
    print("The sum is:",str(addanswer)+".")
else:
    num=float(input("Enter the divident: "))
    denom=float(input("Enter the divisor: "))
    while denom==0.0:
        print("Invalid input.")
        denom=float(input("Enter the divisor: "))
    divanswer=num/denom
    print("The answer is:",str(divanswer)+".")
    
