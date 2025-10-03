# import tkinter
from tkinter import  *



window = Tk()
window.title("Palazzo's Tkinter")
window.minsize(width=400, height=300)


def got_clicked():
    print("i got clicked")
    new_input = input.get()
    label.config(text=new_input)



#the label class
label = Label(text="I am a label")
label.grid(column=0, row=0)



#Button class
button1 = Button(text="Click me", command=got_clicked, bg="black", fg="white")
button2 =Button(text="Hover", command=got_clicked, bg="black", fg="white")
button1.config(padx=50, pady=50)
button1.grid(column=3, row=3)
button2.grid(column=4, row=0)


#Entry class
input = Entry()

input.grid(column=8, row=10)

# def add(*addit):
#     # for a in addit:
#         return sum(addit)
# print(add(3, 9, 10,8,9))


window.mainloop()
