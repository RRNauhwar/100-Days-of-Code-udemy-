import random
print('''  ____
 |    |
 |    O
 |   /|\\
 |   / \\
 |
_|_
|   |______
|          |
|__________|

H A N G M A N
''')
hangman = ['''  ____
 |    |
 |    
 |   
 |    
 |
_|_
|   |______
|          |
|__________|
''','''  ____
 |    |
 |    O
 |   
 |    
 |
_|_
|   |______
|          |
|__________|
''','''  ____
 |    |
 |    O
 |    |
 |    
 |
_|_
|   |______
|          |
|__________|
''','''  ____
 |    |
 |    O
 |   /|
 |    
 |
_|_
|   |______
|          |
|__________|
''','''  ____
 |    |
 |    O
 |   /|\\
 |    
 |
_|_
|   |______
|          |
|__________|
''','''  ____
 |    |
 |    O
 |   /|\\
 |   / 
 |
_|_
|   |______
|          |
|__________|
''','''  ____
 |    |
 |    O
 |   /|\\
 |   / \\
 |
_|_
|   |______
|          |
|__________|
''']
wordlist = [
    # Body parts
    "head", "arm", "leg", "hand", "foot",
    "eye", "ear", "nose", "mouth", "shoulder",
    "knee", "elbow", "wrist", "ankle", "finger",
    "toe", "back", "chest", "stomach", "neck",

    # Creatures
    "dog", "cat", "mouse", "elephant", "tiger",
    "lion", "giraffe", "zebra", "monkey", "horse",
    "cow", "sheep", "goat", "chicken", "duck",
    "fish", "shark", "whale", "dolphin", "penguin",
    "frog", "snake", "lizard", "crocodile", "eagle",
    "sparrow", "parrot", "butterfly", "bee", "ant",

    # Verbs
    "run", "jump", "swim", "fly", "drive",
    "write", "read", "sing", "dance", "eat",
    "drink", "sleep", "walk", "talk", "laugh",
    "cry", "play", "watch", "listen", "cook",
    "paint", "draw", "build", "clean", "wash",
    "throw", "catch", "kick", "hit", "climb"
]

choosen_word = random.choice(wordlist)
#print(choosen_word)
display = []
for letter in choosen_word:
    display+="_"
print(display)
print(hangman[0])
lives=0
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter ").lower()
    for position in range(len(choosen_word)):
       letter = choosen_word[position]
       if letter==guess:
          display[position] = guess
    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives+=1
        if lives == 6:
            end_of_game = True
            print("You lose !")



    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You Win !")

    print(hangman[lives])

