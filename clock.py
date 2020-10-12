from tkinter import *
from time import strftime

root = Tk()
root.title("CLOCK")
root.iconbitmap("P:\My youtube projects\wall-clock.ico")

def time():
    string = strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000,time)
lbl = Label(root, font=("arial", 160,"italic"),bg="white", fg="black")
lbl.pack(anchor = "center", fill="both", expand=1)

time()
root.mainloop()
