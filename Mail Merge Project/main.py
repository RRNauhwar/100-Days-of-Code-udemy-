with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()
with open("Input/Letters/starting_letter.txt") as file:
    tempelate = file.read()
for name in names:
    with open(f"Output/ReadyToSend/{name}.txt",mode="w") as file:
        letter = tempelate.replace("[name]",name)
        file.write(letter)
    
    


