from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("644x344")
root.title("Sliders in Tkinter")
def click():
    print(f"You choose: {range.get()}")
Label(root,text="Choose your range",font="comicsans 13 bold",pady=15).pack()
range=Scale(root,from_=0,to=100,orient=HORIZONTAL,length=300)
range.pack()
Button(root,text="Enter",font=("Arieal",15,"bold"),command=click).pack()

root.mainloop()