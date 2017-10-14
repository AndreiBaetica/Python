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
###########################
#Question 7
###########################
###########################
#Question 8
###########################
###########################
#Question 9
###########################
###########################
#Question 10
###########################
###########################
#Question 11
###########################
###########################
#Question 12
###########################
def time_formater(h,m):
    '''
    (int,int)->none
    Returns time in the format of a sentence.
    Preconditions: TODO
    '''
    if 0>h or h>23:
        print('Invalid hour input.')
        return
    elif 0>m or m>59:
        print('Invalid minute input.')
        return
    m=5*round(m/5)
    t='AM'
    if h>12:
        t='PM'
        h=h-12
    if m==0:
        print('The time is '+str(h)+" o'clock "+t+'.')
    elif m==30:
        print('The time is half past '+str(h),t+'.')
    elif m>30:
        print('The time is '+str(60-m)+' minutes to '+str(h+1),t+'.')
    else:
        print('The time is '+str(m)+' minutes past '+str(h),t+'.')
     
    
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

