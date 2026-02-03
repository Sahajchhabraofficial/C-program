#wap to create window in window.
from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("window-1")
def create():
    win=Tk()
    win.geometry("200x300")
    win.title("window-2")
    win.mainloop()
Button(root,text="Create a new window",font="Helvatica 18 bold",command=create).pack(pady=10)

root.mainloop()