op1=input("Choose one of three functions: a) Multiplication, b) Addition, c) Division: ")
while not (op1=='a' or op1=='b' or op1=='c'):
    print("Invalid input. Type only the lowercase letter corresponding with the desired operation.")
    op1=input("Choose one of three functions: a) Multiplication, b) Addition, c) Division: ")
if op1=='a':
    fac1=input("State how many factors you wish to multiply: ")
    try:
        int(fac1)
    except:
        while ValueError:
            print("Invalid input.")
            fac1=input("State how many factors you wish to multiply: ")
