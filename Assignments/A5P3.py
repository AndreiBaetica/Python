def digit_sum(n):
    '''(int)->int'''
    if n==0:
        return 0
    else:
        return (n%10)+digit_sum(n//10)
    
def digital_root(n):
    '''(int)->int'''
    if n<10:
        return n
    return digital_root(digit_sum(n))
