import math
###########################
#Question 1
###########################
'''
(number)->number
Converts an mph value to kph.
'''
def mh2kh(s):
    s = s*1.609344
    return s

###########################
#Question 2
###########################


###########################
#Question 3
###########################


###########################
#Question 4
###########################

    
###########################
#Question 5
###########################
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

