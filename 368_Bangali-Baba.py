from tkinter import *
import random
from tkinter import messagebox as tmsg

root=Tk()
root.geometry("600x400")
root.title("Bangali baba")
def submit(problem):
    predictions=["    Ha", "    Na", "   Phir Kabhi", "   Bilkul!", "   Kuch keh nahi sakte"]
    if problem!=None:
        tmsg.showinfo("Baba ji keh rahe hai ",f"{random.choice(predictions)} Beta    ")
    else:
        tmsg.showinfo("Baba ji keh rahe hai","    Kya Beta?")
Label(master=root,text="🕉️",font=("Segoe UI Emoji",25,"bold")).pack(pady=4)
Label(master=root,text="Swaagtam Baccha!",font="Arial 17 bold").pack(pady=4)
Label(master=root,text="! sach aur jhoot ka pata karein !",font="Arial 17").pack(pady=4)
samasya=Entry(master=root,borderwidth=5,width=50,relief=SUNKEN).pack(pady=4)
Button(master=root,text="Submit",font="Helvatice 14",command=lambda:submit((samasya))).pack(pady=4)

root.mainloop()