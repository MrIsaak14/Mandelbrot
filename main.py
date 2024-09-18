import math
from tkinter import Frame
from tkinter import Label, Button, Entry

s

scherm=Frame()

scherm.configure(background="blue")
scherm.configure(width=200, height=100)
scherm.master.title("mandelbrot")
scherm.pack()

knop=Button(scherm)

knop.configure(text="Start")
knop.place(x=100, y=10)

invoer=Entry(scherm)
invoer.place(x=150, y=70)





scherm.mainloop()