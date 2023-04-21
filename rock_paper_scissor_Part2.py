import random 
#Rock - Paper - Scissor Game 

def play():
   
    wins = 0
    losses = 0
    draws = 0

    while True:

        user = input(" What's your choice or e to Exit ? 'r' for rock, 'p' for paper, 's' for scissors ")
        computer = random.choice(['r','p','s'])
        
        if user == "e":
            break

        if user not in ['r','p','s']:
            continue

        if user == computer:
            print("It's a tie")
            draws += 1
            
        #r >s, s > p, p > r
        elif is_win(user, computer):
            print("You won!")
            wins += 1
            
        #if is_win(user, computer):
        else:
            print("You lost!")
            losses += 1
    
    print(f"\nYou won {wins} times. ")
    print(f"You lost {losses} times.")
    print(f"You drew {draws} times. ")
    return ""

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True
    
print(play())