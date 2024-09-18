import math
from tkinter import Frame
from tkinter import Label, Button, Entry

scherm=Frame()

scherm.configure(background="light grey")
scherm.configure(width=1000, height=700)
scherm.master.title("mandelbrot")
scherm.pack()

knop=Button(scherm)

knop.configure(text="Start")
knop.place(x=10, y=130)

#invoor midden X
invoerX=Entry(scherm)
invoerX.place(x=90, y=10)
uitvoer=Label(scherm)
uitvoer.configure(text="Midden X:")
uitvoer.place(x=10, y=10)


#invoer midden Y
invoerY=Entry(scherm)
invoerY.place(x=90, y=40)
uitvoer=Label(scherm)
uitvoer.configure(text="Midden Y:")
uitvoer.place(x=10, y=40)


#invoer schaal
invoerS=Entry(scherm)
invoerS.place(x=90, y=70)
uitvoer=Label(scherm)
uitvoer.configure(text="Schaal:")
uitvoer.place(x=10, y=70)


#invoer max aantal
invoerA=Entry(scherm)
invoerA.place(x=90, y=100)
uitvoer=Label(scherm)
uitvoer.configure(text="Max aantal:")
uitvoer.place(x=10, y=100)


#functie mandelbrot
x = float(invoerX.get())
y = float(invoerY.get())
a = 0
b = 0
mand = 0
while mand < invoerA and math.sqrt((x - a)**2 + (y - b)**2) < 2:
    a = (a**2 - b**2 + x)
    b = (a**2 - b**2 + y)
    mand += 1
    

scherm.mainloop()