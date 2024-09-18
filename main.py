import math
from tkinter import Frame
from tkinter import Label, Button, Entry

#functie mandelbrot
def mandelbrot():
    x = float(invoerX.get())
    y = float(invoerY.get())
    maxAantal = float(invoerA.get())
    a = 0
    b = 0
    mand = 0
    while mand < maxAantal and math.sqrt((x - a)**2 + (y - b)**2) < 2:
        a = (a**2 - b**2 + x)
        b = (a**2 - b**2 + y)
        mand += 1
    printFunction.configure(text=f"{a} {b} {mand}")

scherm = Frame(background="light grey", width=1000, height=700)
scherm.master.title("mandelbrot")
scherm.pack()

knop = Button(scherm, text="Start", command=mandelbrot)
knop.place(x=10, y=130)

#invoor midden X
invoerX = Entry(scherm)
invoerX.place(x=90, y=10)
uitvoerX = Label(scherm, text="Midden X:")
uitvoerX.place(x=10, y=10)


#invoer midden Y
invoerY = Entry(scherm)
invoerY.place(x=90, y=40)
uitvoerY = Label(scherm, text="Midden Y:")
uitvoerY.place(x=10, y=40)


#invoer schaal
invoerS = Entry(scherm)
invoerS.place(x=90, y=70)
uitvoerS = Label(scherm, text="Schaal:")
uitvoerS.place(x=10, y=70)


#invoer max aantal
invoerA = Entry(scherm)
invoerA.place(x=90, y=100)
uitvoerA = Label(scherm, text="Max aantal:")
uitvoerA.place(x=10, y=100)

printFunction = Label(scherm, text="...")
printFunction.place(x=10, y=160)

scherm.mainloop()