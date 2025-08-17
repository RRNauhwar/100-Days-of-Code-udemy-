from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.minsize(height=200, width=300)
window.config(padx=20, pady=20)

# Entry
input_box = Entry(width=10)
input_box.grid(column=0, row=0)

# Unit label
unit = Label(text="Miles", font=("Arial", 14))
unit.grid(column=1, row=0)

# Conversion labels
label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

result = Label(text="0 Km", font=("Arial", 14))
result.grid(column=1, row=1)

# Button function
def calculate_miles():
    try:
        miles = float(input_box.get())  # convert string to float
        km = round(miles * 1.609, 2)   # round to 2 decimals
        result["text"] = f"{km} Km"
    except ValueError:
        result["text"] = "Invalid Input"

# Button
calculate = Button(text="Calculate", command=calculate_miles)
calculate.grid(column=1, row=2)

window.mainloop()

