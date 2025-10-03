from tkinter import *


window = Tk()
window.title("Palazzo's Miles To Km Converter.")
window.minsize(width=200, height=200)
window.config(pady=100, padx=100)

#TODO 4: create a function that converts your input to km
def convert():
    try:
        new_input = float(input_for_miles.get()) * 1.60934
    except ValueError:
        new_input = None
    answer.config(text=new_input)


#TODO 1: create Labels
equal = Label(text="Is equal to:")
miles = Label(text="Miles")
km = Label(text="Km")
answer = Label(text="0")

equal.grid(column=0, row=2)
miles.grid(column=3, row=1)
km.grid(column=3, row=2)
answer.grid(column=1, row =2)


#TODO 2: create input
input_for_miles = Entry()
input_for_miles.grid(column=1, row=1)




#TODO 3: create the calculate button
calculate = Button(text="Convert", command=convert)
calculate.grid(column=1, row= 4)

















window.mainloop()