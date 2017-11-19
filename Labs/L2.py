import math

def repeater(s1, s2, n):
     ''' (str,str,int)->str
     Returns a silly string: i.e. s1 and s2 concatinated
     and repeated n times and deliminated by underscore '''
     
     s=s1+s2
     return "_"+(s*n)+"_"

def reverse(x):
     ''' (int)->int
     Returns integer x with reversed digits

     Precondition: x is a two digit positive integer
     '''
     
     high_digit = x // 10
     low_digit = x % 10
     return low_digit * 10 + high_digit

def roots(a, b, c):
     ''' (number, number,number)->number
     Prints nicely the soluitons of the quadratic equation
     with ccoefficients a, b, c

     Precondition: a is not equal to zero and
                   b*b-4ac is not a negative number '''
     x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
     x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
     print ("The quadratic equation with coefficients a =", a, "b =", b, "c =", c)
     print ("has the following solutions (i.e. roots): ")
     print (x1, " and", x2)

def real_roots(a, b, c):
     ''' (number, number,number)->boolean

     Returns True if the quadratic equation with
     coefficients a, b, c has real roots. False otherwise'''

     return b**2-4*a*c >= 0
