print("Welcome to the tip calculator!")
cost = float(input("What was the total bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))
final_pay = (cost+(1+tip*0.01))/people
print("Each person should pay: ${final_pay}")
