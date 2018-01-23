import random
snakepos={11:2,25:4,38:9,65:46,89:70,93:64}
ladderpos={8:37,13:34,40:68,52:81,76:97}s
def generate_random():
    '''
    A function to return a random number between 1 and 12 to roll the dice
    '''
    return random.randrange(1,13)
def get_player_dict(n):
    adict={}
    for i in range(1,n+1):
        a=input("Enter the name of player "+str(i)+" : ")
        adict[a]=0
    return adict

