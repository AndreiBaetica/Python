
import operator
import functools

op1=input("Choose one of three functions: a) Multiplication, b) Addition, c) Division: ")
while not (op1=='a' or op1=='b' or op1=='c'):
    print("Invalid input. Type only the lowercase letter corresponding with the desired operation.")
    op1=input("Choose one of three functions: a) Multiplication, b) Addition, c) Division: ")
if op1=='a':
    fac1=input("State how many factors you wish to multiply: ")
    while 1==1:
        try:
            int(fac1)
            break
        except ValueError or fac1=='1':
            print("Invalid input.")
            fac1=input("State how many factors you wish to multiply: ")
    f1=input("Enter the first factor: ")
    while 1==1:
        try:
            float(f1)
            break
        except ValueError:
            print("Invalid input.")
            f1=input("Enter the first factor: ")
    multlist=[float(f1)]
    multinput=0
    while multinput<int(fac1)-1:
        fn=input("Enter the next factor: ")
        while 1==1:
            try:
                float(fn)
                break
            except ValueError:
                print("Invalid input.")
                fn=input("Enter a valid response: ")
        multlist.append(float(fn))
        multinput=multinput+1
    multanswer=functools.reduce(operator.mul,multlist,1)
    print("The product is:",str(multanswer)+".")
elif op1=='b':
    add1=input("State how many numbers you wish to add: ")
    while 1==1:
        try:
            int(add1)
            break
        except ValueError or add1=='1':
            print("Invalid input.")
            add1=input("State how many numbers you wish to add: ")
    a1=input("Enter the first number: ")
    while 1==1:
        try:
            float(a1)
            break
        except ValueError:
            print("Invalid input.")
            a1=input("Enter the first number: ")    
    addlist=[float(a1)]
    addinput=0
    while addinput<int(add1)-1:
        an=input("Enter the next number: ")
        while 1==1:
            try:
                float(an)
                break
            except ValueError:
                print("Invalid input.")
                an=input("Enter the next number: ")    
        addlist.append(float(an))
        addinput=addinput+1
    addanswer=sum(addlist)
    print("The sum is:",str(addanswer)+".")
else:
    num=input("Enter the divident: ")
    while 1==1:
        try:
            float(num)
            break
        except ValueError:
            print("Invalid input.")
            num=input("Enter the divident: ")
    denom=input("Enter the divisor: ")
    while 1==1:
        try:
            float(denom)
            break
        except ValueError:
            print("Invalid input.")
            denom=input("Enter the divisor: ")
    while 1==1:
        try:
            divanswer=float(num)/float(denom)
            break
        except ZeroDivisionError:
            print("Invalid input, cannot divide by zero.")
            denom=input("Enter the divisor: ")
    print("The answer is:",str(divanswer)+".")
    
