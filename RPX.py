import random

def play():
    user = input(" [r] for Rock, [p] Paper, [x] Scissors : ")
    computer=random.choice(['r','p','x'])
    
    if user == computer:
        return 'tie'
    
    if is_win(user,computer):
        return 'Your Won !!!!!!'
    
    return 'You Lost :( '
    #r<p , p<x r>p
    #r>x , x>p, p>r
    
def is_win(player,opponent):
        #r>x , x>p, p>r
        #return true if the player win
        
        if (player =='r' and opponent=='x') or (player =='x' and opponent=='p') or (player=='p' and opponent=='r'):
            return True
        
#to start playing
print(play())