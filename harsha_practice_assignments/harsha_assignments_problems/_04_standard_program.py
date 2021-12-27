
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Harsha_practice_clock")

def time():
    string1=strftime('%I:%M:%S %p')
    label.config(text=string1)
    label.after(1000,time)

label=Label(root,font=('Times New Roman Greek',60),background='black',foreground='cyan')
label.pack()

time()
mainloop()
