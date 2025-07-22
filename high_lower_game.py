import random
import os 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from art import higherLower_logo, higherLower_vs
from highlowerGameData import data
def random_account():
    return random.choice(data)

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."
def compare(guess,a_followerscount,b_followerscount):
    if a_followerscount>b_followerscount:
        return guess=="a"
    else:
        return guess=="b"
    
def game ():
    print(higherLower_logo)
    score = 0
    a = random_account()
    b = random_account()
    is_game_continue = True
    while is_game_continue:
        a=b
        b=random_account()
        while a['follower_count']==b['follower_count']:
          b = random_account()
        print(f"Compare A: {format_data(a)}")
        print(higherLower_vs)
        print(f"Against B: {format_data(b)}")
        guess = input("Who has more followers? Type 'A' and 'B': ").lower()
        isCorrect = compare(guess,a['follower_count'],b['follower_count'])
        clear()
        print(higherLower_logo)
        if isCorrect:
          score+=1
          print(f"You're right! Current score : {score}.")
        else:
          
          print(f"Sorry that's wrong. Final score: {score}.")
          is_game_continue = False

game()