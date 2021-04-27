# python '3-rock-paper-scissors.py'
import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','s','p'])

    if computer == user:
        return 'it\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player , computer):
    if (player== 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
    
    return False

print(play())