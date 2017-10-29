import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    return random.shuffle(deck)

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    discovered[p1]=original_board[p1]
    discovered[p2]=original_board[p2]
    
    print_board(discovered)
    
    
    

#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    # YOUR CODE GOES HERE
    playable_board=l
    playable_board.remove('*')
    for i in playable_board:
        if playable_board.count(i) != 2:
            playable_board.remove(i)
    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE
    for i in l:
        if l.count(i) != 2:
            return None
    return True
                
        

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE
    discovered=[]
    discovered_count=0
    while discovered_count <= len(board)-1:
        discovered.append('*')
        discovered_count=discovered_count+1
    
    
    tries=0
    
    while discovered!=board:
        print_board(discovered)
        print('\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, '+str(len(board)+1)+']')
        p1=int(input('\nEnter position 1: '))
        p1=p1-1
        p2=int(input('Enter position 2: '))
        p2=p2-1
        while p1==p2:
            print('Invalid input. Position 1 cannot equal position 2. \nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, '+str(len(board)+1)+']')
            p1=int(input('\nEnter position 1: '))
            p1=p1-1
            p2=int(input('Enter position 2: '))
            p2=p2-1
            print('This try did not count. Total tries: '+str(tries))
        while discovered[p1]==board[p1]:
            print('Invalid input. Position 1 has already been revealed. \nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, '+str(len(board)+1)+']')
            p1=int(input('\nEnter position 1: '))
            p1=p1-1
            p2=int(input('Enter position 2: '))
            p2=p2-1
            print('This try did not count. Total tries: '+str(tries))
        while discovered[p2]==board[p2]:
            print('Invalid input. Position 2 has already been revealed. \nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, '+str(len(board)+1)+']')
            p1=int(input('\nEnter position 1: '))
            p1=p1-1
            p2=int(input('Enter position 2: '))
            p2=p2-1
            print('This try did not count. Total tries: '+str(tries))
        while discovered[p1]==board[p1] and discovered[p2]==board[p2]:
            print('Invalid input. Both positions have already been revealed. \nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1, '+str(len(board)+1)+']')
            p1=int(input('\nEnter position 1: '))
            p1=p1-1
            p2=int(input('Enter position 2: '))
            p2=p2-1
            print('This try did not count. Total tries: '+str(tries))
        
        print_revealed(discovered, p1, p2, board)
        if discovered[p1]!=discovered[p2]:
            discovered[p1]='*'
            discovered[p2]='*'
        print()
        wait_for_player()
        print('\n'*20)

        tries=tries+1

    
    print('Congratulations! You completed the game with '+str(tries)+' guesses. That is '+str(len(board)//2)+' more than the best possible.')

    



#main
    
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE
def ascii_name_plaque(name):
    '''
    (str)->none
    Prints the name surrounded by a box of *
    '''
    print((10+len(name))*'*')
    print('*'+(8+len(name))*' '+'*')
    print('*  __'+name+'__  *')
    print('*'+(8+len(name))*' '+'*')
    print((10+len(name))*'*')
ascii_name_plaque('Welcome to my Concentration game')

choice = input('Would you like (enter 1 or 2 to indicate your choice): \n(1) me to generate a rigorous deck of cards for you \n(2) or, would you like me to read a deck from a file?\n')
while True:
    try:
        choice=int(choice)
        if choice != 1 and choice != 2:
            choice=input(str(choice)+' is not existing option. Please try again. Enter 1 or 2 to indicate your choice\n')
        else:
            break
    except ValueError:
        choice=input(str(choice)+' is not existing option. Please try again. Enter 1 or 2 to indicate your choice\n')
        
# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
if choice==1:
    print('You have chosen to have a rigorous deck generated for you \n')
    size = input('How many cards do you want to play with? \n Enter an even number between 0 and 52: ')
    while True:
        try:
            size=int(size)
            if 2<=size<=52 and size%2==0:
                break
            else:
                size = input('How many cards do you want to play with? \n Enter an even number between 0 and 52: ')
        except ValueError:
            size = input('How many cards do you want to play with? \n Enter an even number between 0 and 52: ')
    board=create_board(size)
    print("Shuffling the deck...")
    shuffle_deck(board)
    print()
    wait_for_player()
    print('\n'*20)
    play_game(board)
    

# YOUR CODE FOR OPTION 2 GOES HERE
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another
#
#print("You chose to load a deck of cards from a file")
#file=input("Enter the name of the file: ")
#file=file.strip()
#board=read_raw_board(file)
#board=clean_up_board(board)


