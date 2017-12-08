def largest_34(a):
    '''
    (list)->number
    '''
    a=sorted(a)
    return(a[-3]+a[-4])

def largest_third(a):
    '''
    (list)->int
    '''
    a=sorted(a)
    j=-1
    a2=[]
    for i in range(len(a)//3):
        a2.append(a[j])
        j=j-1
    return sum(a2)

def third_at_least(a):
    '''
    (list)->element or None
    Note: element in this case refers to elements contained in list a.
    '''
    for i in a:
        if a.count(i)>=(len(a)//3+1):
        # count has O(n) complexity
            return i
    return None

def sum_tri(a,x):
    '''
    (list,number)->boolean
    '''
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if a[i]+a[j]+a[k]==x:
                    return True
    return False
