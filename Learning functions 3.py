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

