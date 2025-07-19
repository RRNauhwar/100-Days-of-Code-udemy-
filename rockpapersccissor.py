import random
a= int(input("Let's play, type 1 for 'ROCK' 2 for 'PAPER' 3 for 'SCISSOR'. "))
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

b = random.randint(1,3)
if b == a:
    print("Computer chose the same, It is a TIE")
    if (a==1):
        print(f"Your response: Rock\n {rock}\n Computer response: Rock\n {rock}")
    elif(a==2):
        print(f"Your response: Paper\n {paper}\n Computer response: Paper\n {paper}")
    elif(a==3):
        print(f"Your response: Scissor\n {scissor}\n Computer response: Scissor\n {scissor}")
elif (a==1 and b==2):
    print(f"COMPUTER WINS! Your response: Rock\n {rock}\n Computer response: Paper\n {paper}")
elif(a==1 and b==3):
    print(f"CONGRATULATIONS! YOU WIN ! Your response: Rock\n {rock}\n Computer response: Scissor\n {scissor}")
elif(a==2 and b==3):
    print(f"COMPUTER WINS! Your response: Paper\n {paper}\n Computer response: Scissor\n {scissor}")
elif(a==2 and b==1):
    print(f"CONGRATULATIONS! YOU WIN ! Your response: Paper\n {paper}\n Computer response: Rock\n {rock}")
elif(a==3 and b==1):
    print(f"COMPUTER WINS! Your response: \n{scissor}\n Computer response: \n{rock}")
elif(a==3 and b==2):
    print(f"CONGRATULATIONS ! YOU WIN ! Your response: \n{scissor}\n Computer response: \n{paper}")
else:
  print("Invalid Input")
      
