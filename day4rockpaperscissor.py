import random 
user_choice= int(input("Let's play, type 0 for 'ROCK' 1 for 'PAPER' 2 for 'SCISSOR'. "))
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
scissor ='''     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
game_choices = [rock,paper,scissor]
computer_choice = random.randint(0,2)
print(f"You choose: \n {game_choices[user_choice]}")
if (user_choice>=3 or user_choice<0):
    print("Invalid number, You lose!")
elif(user_choice == 2 and computer_choice == 0):
    print(f"Computer choose: \n {game_choices[computer_choice]},\nYou lose!")
elif(user_choice == 0 and computer_choice == 2):
    print(f"Computer choose: ]\n {game_choices[computer_choice]},\nYou win!")
elif(user_choice<computer_choice):
    print(f"Computer choose: ]\n {game_choices[computer_choice]},\nYou lose!")
elif(user_choice>computer_choice):
    print(f"Computer choose: ]\n {game_choices[computer_choice]},\nYou win!")
else:
    print(f"Computer choose: ]\n {game_choices[computer_choice]},\nIt is a draw! !")
