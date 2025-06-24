import random
symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*"]
number_list = ["1","2","3","4","5","6","7","8","9","0"]
alphabet_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print("Welcome to the PyPassword Generator!")
length = int(input("How many letters would you like in your password?"))
symbols = int(input("How many symbols would you like?"))
numbers = int(input("How many numbers would you like?"))
letters = length - symbols-numbers
passwordList = []
for char in range(1,letters+1):
    passwordList.append(random.choice(alphabet_list))
for char in range(1,symbols+1):
    passwordList.append(random.choice(symbol_list))
for char in range(1,numbers+1):
    passwordList.append(random.choice(number_list))
random.shuffle(passwordList)
password = "".join(passwordList)
print(password)
