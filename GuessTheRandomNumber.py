from tkinter import *
import random

fenster = Tk()

frame = Frame(fenster)
frame.pack()

midFrame = Frame(fenster, relief=RIDGE, bd=2)
midFrame.pack()

bottomFrame = Frame(fenster)
bottomFrame.pack(side=BOTTOM)

fenster.title("Zahlenraten")
fenster.geometry("300x300")

zahl = random.randint(0, 100)
print(zahl)

versuch = 1
eingabe_var = IntVar()


def lesen():
    global versuch
    versuchText = "{} . Versuch".format(versuch)
    userInput = int(name_entry.get())

    print(userInput)
    if userInput > zahl:
        text1 = "Eingabe > Zahl"
        label4.configure(text=text1)
        versuch = versuch + 1
        label3.configure(text=versuchText)

    elif userInput < zahl:
        label4.configure(text="Eingabe < Zahl")
        versuch = versuch + 1
        label3.configure(text=versuchText)

    else:
        label4.configure(text="Richtig!")

def neuStarten():
    global versuch
    print("Neu Start!")
    label4.configure(text="")
    versuch = 1
    label3.configure(text="0. Versuch")
    zahl = random.randint(0, 100)
    print(zahl)


label1 = Label(frame, font=("Arial black", 30), text="Zahlenraten")
label1.pack()

label2 = Label(frame, text="Errate die Zahl zwischen 1 und 100", font=("Arial", 12))
label2.pack()

label3 = Label(midFrame, text="0. Versuch")
label3.pack(side=TOP)

label4 = Label(midFrame, text="")
label4.pack(side=BOTTOM)

name_entry = Entry(midFrame, textvariable=eingabe_var, font=('calibre', 10, 'normal'), width=5, justify=CENTER)
name_entry.pack(side=LEFT)

button1 = Button(midFrame, text="Tipp abgeben", command=lesen)
button1.pack(side=LEFT)

button2 = Button(bottomFrame, text="neu Starten", command=neuStarten)
button2.pack()

fenster.mainloop()