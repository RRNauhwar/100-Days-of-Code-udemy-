import os

def clear():
    # Clears the screen based on the OS
    os.system('cls' if os.name == 'nt' else 'clear')

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

auction = {}
end_of_auction = False

def winner_of_auction(auction):
    max_bid = 0
    winner = ""
    for key in auction:
        if max_bid <= auction[key]:
            max_bid = auction[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${max_bid}")

while not end_of_auction:
    name = input("What is the name of the bidder? ")
    bid = int(input("Input the bid amount: $"))
    auction[name] = bid
    response = input("Are there other users who want to bid? (yes/no) ").lower()
    if response == "yes":
        end_of_auction = False
        clear()
    elif response == "no":
        end_of_auction = True
        winner_of_auction(auction)
    else:
        print("Invalid response. Ending auction.")
        end_of_auction = True
        winner_of_auction(auction)
