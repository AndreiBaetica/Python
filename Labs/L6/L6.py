# Problem 5.16
# counter loop pattern
def indexes(word, letter):
    '''Returns a list of indexes at which character letter appears in word'''
    res = []
    for i in range(len(word)):
        if word[i] == letter:
            res.append(i)
    return res



# Problem 5.17
# counter loop pattern
def doubles(l):
    '''Prints integers in list l that are exactly twice
       the previous integer in the list'''
    for i in range(1, len(l)):
        if l[i] == 2*l[i-1]:
            print(l[i])



# Problem 5.18
# iteration and accumulator loop patterns
def four_letter(lst):
    '''Returns list of 4-letter words in list of strings lst'''
    res = []
    for word in lst:
        if len(word) == 4:
            res.append(word)
    return res



# Problem 5.19
# iteration and nested loop patterns
def inBoth(lst1, lst2):
    '''Returns True if there is an item that is common to lists lst1 and lst2,
    and False otherwise'''
    for item in lst1:
        if item in lst2:
            return True
    return False



# Problem 5.20
# iteration loop pattern
def intersect(lst1, lst2):
    '''Returns the list of items common to lists lst1 and lst2,
       neither containing duplicate items'''
    res = []
    for item in lst1:
        if item in lst2:
            res.append(item)
    return res



# Problem 5.21
# counter and nested loop patterns
def pair(lst1, lst2, x):
    '''Prints the pairs of integers, one from list lst1 and the other
       from list lst2, that add up to n'''
    for i in lst1:
        for j in lst2:
            if i + j == x:
                print(i, j)



# Problem 5.22
# counter and nested loop patterns
def pairSum(lst, x):
    '''Prints the indexes of all pairs of values in list lst that sum up to n'''
    for i in range(len(lst)-1):        # left index in pair
        for j in range(i+1,(len(lst))):  # right index in pair
            if lst[i]+lst[j] == x:
                print(i,j)




# Problem 5.29
def lastfirst(lst):
    '''lst is a list of strings of the format <LastName, FirstName>;
       function returns a list consisting two lists: a list of all the
       first names and a list of all the last names'''
    first = []
    last = []
    for s in lst:
        pair = s.split(', ')
        last.append(pair[0])
        first.append(pair[1])
    return [first, last]


# Problem 5.31
def subsetSum(lst, target):
    '''Returns True if there are 3 numbers in list lst that add up to target number,
       and False otherwise'''
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                if lst[i] + lst[j] + lst[k] == target:
                    return True
    return False
                

# Problem 5.33
def mystery(x):
    '''Returns the number of times necessary te halve n
       (using integer division) before reaching 1'''
    i = 0
    while x > 1:
        x //= 2
        i += 1
    return i




# Problem 5.37
def mssl(lst):
    '''Returns the sum of the maximum sum sublist of list lst'''
    best = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            total = 0
            for k in range(i, j):
                total += lst[k]
            if total > best:
                best = total
    return best




# Problem 5.46
def inversions(s):
    '''Returns the number of inversions in sequence s'''
    res = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] > s[j]:
                res += 1
    return res


# Problem 5.48
def sublist(lst1, lst2):
    ''' Returns True if list lst1 is a sublist of list lst2, and False otherwise'''
    index1 = 0                # lst1 index
    index2 = 0                # lst2 index

    # go through indexes of lst1
    while index1 < len(lst1):
        
        # search for item in lst2 matching item in lst1 at index index1
        while index2 < len(lst2) and lst1[index1] != lst2[index2]:
            index2+=1

        # if we run out of items in lst2, lst1 is not a sublist of lst2
        if index2 == len(lst2):
            return False
        index1 += 1

    # every item in lst1 has been matched to an item in lst2, from left to right
    return True

