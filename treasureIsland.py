print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
cmd1 = input("TYPE 'left' or 'right' ").lower()
if(cmd1== "left" ):
    print("You've come to a lake. There is an island in the middle of the lake.")
    cmd2 = input("TYPE 'wait' to wait for a boat. TYPE 'swim' to swim across.").lower()
    if(cmd2=="wait"):
        print("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue.")
        cmd3 = input("Which colour do you choose?").lower()
        if(cmd3=="yellow"):
            print("Congratulations! you win.")
        elif(cmd3=="red"):
            print("Burned by fire. GAME OVER.")
        elif(cmd3=="blue"):
            print("Eaten by beasts. GAME OVER.")
        else:
            print("GAME OVER.")
    else:
        print("Attacked by trout. GAME OVER.")
else:
    print("Fall into a hole. GAME OVER.")
