
def pay(wage,hours):
    
    if hours <= 40:
        salary = hours * wage
    elif (hours > 40 and hours <= 60):
        salary = (40 * wage) + (hours - 40)*(1.5*wage)
    elif (hours > 60):
        salary = (40 * wage) + (20)*(1.5*wage) + (hours - 60)*(2*wage)

    return salary

def rps(play1, play2):
    '''    (str, str)->int

       takes choices ('R', 'P', or 'S') of player 1 and 2,
       and returns -1 if player 1 wins, 1 if player 2 wins,
       or 0 if there is a tie'''
    
    if play1 == play2:
        return 0
    if (play1 == 'P' and play2 == 'R') or (play1 == 'R' and play2 == 'S') or (play1 == 'S' and play2 == 'P'):
        return -1
    else:
        return 1
