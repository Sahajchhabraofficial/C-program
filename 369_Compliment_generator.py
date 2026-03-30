from tkinter import *
import customtkinter as ctk
import random
import tkinter.messagebox as tmsg

root=ctk.CTk()
root.geometry("600x400")
root.title("Random Compliment Generator")
root.minsize(600,400)
def enter():
    # global entry
    name=entry.get()
    if name=="":
        tmsg.showinfo("Error","Please enter your name!")
        return
    compliments=["You are amazing!","You have a great sense of humor!","You are so talented!","You have a beautiful smile!","You are a great listener!"]
    compliment=random.choice(compliments)
    tmsg.showinfo("Compliment", f"{compliment} {name}!")
Label(root,text="Hello! Can i know your name?",font="Arial 17 bold").pack(pady=4)
entry=Entry(root,borderwidth=5,width=50,relief=SUNKEN)
entry.pack(pady=4)
Button(root,text="Enter",borderwidth=5,font="Helvatice 14",command=enter).pack(pady=4)

root.mainloop()