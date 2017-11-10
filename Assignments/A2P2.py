def min_enclosing_rectangle(radius,x,y):
    '''
    (number,number,number)->(number,number) or None
    Gives lower left coordinate of a rectangle with minimal area that encompasses a circle defined by
    radius, x, and y (origin coordinates).
    Precondition: radius<0
    '''
    if radius<0:
        return None
    cxl=x-radius
    cyb=y-radius
    return(cxl,cyb)


def series_sum():
    '''
    (none)->number
    Prompts user for input n and returns 1000+sigma[1,n][1/n^2].
    '''
    n=int(input('Please enter a non-negative integer: '))
    if n<0:
        return None
    else:
        i=1
        sum=1000
        while i<n+1:
            sum=sum+(1/(i**2))
            i=i+1
        return sum
    
def pell(n):
    '''
    (int)->int or None
    Returns nth Pell number.
    Precondition: n>=0
    '''
    if n<0:
        return None
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return(2*pell(n-1)+pell(n-2))

    
def countMembers(s):
    '''
    (str)->int
    returns number of special characters in s.
    '''
    list=['e','f','g','h','i','j','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','2','3','4','5','6','!',',','\\']
    tally=0
    for i in s:
        if i in list:
            tally=tally+1
    return tally

def casual_number(s):
    '''
    (str)->int
    Removes commas from numbers.
    '''
    try:
        return int(s.replace(',',''))
    except ValueError:
        return None

    
def alienNumbers(s):
    '''
    (str)->int
    Translates alien symbol sequences into numbers.
    Preconditions: s is comprised only of alien symbols.
    '''
    list=[]
    for i in s:
        list.append(i)
    for idx, i in enumerate(list):
        if list[idx]=='T':
            list[idx]=1024
        if list[idx]=='y':
            list[idx]=598
        if list[idx]=='!':
            list[idx]=121
        if list[idx]=='a':
            list[idx]=42
        if list[idx]=='N':
            list[idx]=6
        if list[idx]=='U':
            list[idx]=1
    return sum(list)
