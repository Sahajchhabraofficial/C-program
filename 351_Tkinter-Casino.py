from tkinter import *
import random
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk

self=Tk()
self.title("Tkinter Casino")
self.geometry("1920x1080")
self.minsize(600,400)

def get_started():
    start=Toplevel()  # Changed from Tk() to Toplevel()
    start.title("Game selection")
    start.geometry("1920x1080")
    start_f1=Frame(start,bg="white",relief="groove")
    start_f1.pack(pady=250)
    Label(start_f1,text="Select your game please",font=("baskerville old face",19,"bold"),bg="white").pack()
    Jackpot=Button(start_f1,text="Jackpot",font="Helvatica 14 italic",bg="white")
    Jackpot.pack(pady=10,padx=80,side=LEFT)
    Coming_soon=Button(start_f1,text="Coming Soon",font="Helvatica 14 italic",bg="white")
    Coming_soon.pack(pady=10,padx=80,side=LEFT)
    
    Jackpot_imagePath="C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\jackpot.jpg"
    Jackpot_image=Image.open(Jackpot_imagePath)
    tk_Jackpot=ImageTk.PhotoImage(Jackpot_image)
    Jackpot_image_label=Label(start_f1,image=tk_Jackpot)
    Jackpot_image_label.image = tk_Jackpot  # FIXED: Keep reference to prevent garbage collection
    Jackpot_image=Jackpot_image.resize((10,20),Image.Resampling.LANCZOS)
    Jackpot_image_label.pack(pady=10,padx=80,side=LEFT)

frame=Frame(self,bg="white",relief="flat")
frame.pack(pady=350)
Label(frame,text="Welcome to Casino",bg="white",font=("baskerville old face", 26, "bold"),fg="red").pack(pady=5,padx=5)
Label(frame,
      text="""Test your luck and sharpen your skills with our collection of classic casino games. 
      Place your bets, spin the wheels, and watch your virtual chips grow. 
      Remember - it's all about entertainment, so play responsibly and enjoy the excitement!""",
      font="Helvatica 14",
      fg="grey",
      bg="white"
      ).pack(pady=5,padx=5)
Button(frame,text="Get Started",font="Roboto 10 bold",height=1,bg="white",command=get_started).pack(pady=5,ipady=5,ipadx=5,padx=5)

self.mainloop()