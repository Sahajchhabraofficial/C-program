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
    start_f1.pack(pady=4)
    start_f2=Frame(start,bg="white",relief="groove")
    start_f2.pack(pady=4)
    def start_game():
        start_game=Tk()
        start_game.title("Jackpot 777")
        start_game.geometry("1920x1080")
        Label(start_game,text="What is your account balance?",font=("Agency FB",20,"bold"),bg="white").pack(pady=5)
        bal=Entry(start_game,font="Helvatica 14",bg="white",width=20)
        bal.pack(pady=5)
        tmsg.showinfo("Warning","--==play at your own risk==--")
        Label(start_game,text="How much do you bet?",font=("Agency FB",20,"bold")).pack(pady=5)
        ent=Entry(start_game,width=20)
        ent.pack(pady=5)
        Bet=ent.get()
        balance=bal.get()
        initial_balance=balance
        Button(start_game,text="Play",font=("Agency FB",15,"bold"),command=lambda: jackpot(initial_balance,Bet,balance)).pack(pady=5)

        start_game.mainloop()
    Label(start_f1,text="Select your game please!",font=("baskerville old face",19,"bold"),bg="white").pack()
    Jackpot=Button(start_f2,text="Jackpot",font="Helvatica 14 italic",bg="white",command=start_game)
    Jackpot.grid(row=1,column=1,pady=5,padx=4)
    Coming_soon=Button(start_f2,text="Coming Soon",font="Helvatica 14 italic",bg="white")
    Coming_soon.grid(row=2,column=1,pady=5,padx=4)
    
    Jackpot_imagePath="C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\jackpot.jpg"
    Jackpot_image=Image.open(Jackpot_imagePath)
    Jackpot_image=Jackpot_image.resize((150,150),Image.Resampling.LANCZOS)
    tk_Jackpot=ImageTk.PhotoImage(Jackpot_image)
    Jackpot_image_label=Label(start_f2,image=tk_Jackpot)
    Jackpot_image_label.image = tk_Jackpot
    Jackpot_image_label.grid(row=2,column=2,pady=5,padx=4)
    
    Coming_soon_imagePath="C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\Question mark.jpg"
    Coming_soon_image=Image.open(Coming_soon_imagePath)
    Coming_soon_image=Coming_soon_image.resize((150,150),Image.Resampling.LANCZOS)
    tk_Coming_soon=ImageTk.PhotoImage(Coming_soon_image)
    Coming_soon_image_label=Label(start_f2,image=tk_Coming_soon)
    Coming_soon_image_label.image = tk_Coming_soon
    Coming_soon_image_label.grid(row=1,column=2,pady=5,padx=4)

    # Coming_soon_imagePath="C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\Question mark.jpg"
    # Coming_soon_image=Image.open(Coming_soon_imagePath)
    # tk_Coming_soon=ImageTk.PhotoImage(Coming_soon_image)
    # Coming_soon_image_label=Label(start_f1,image=tk_Coming_soon)
    # Coming_soon_image_label.image = tk_Coming_soon
    # Coming_soon_image=Coming_soon_image.resize((10,20),Image.Resampling.LANCZOS)
    # Coming_soon_image_label.pack(side=TOP)
    def jackpot(ini_bal,bet,balance):
        initial_balance=ini_bal
        Balance=int(ini_bal)
        Bet=bet
        while True:
            if Balance>0:
                bet_value=Bet
                try:
                    bet_value=int(bet_value)
                except ValueError:
                    tmsg.showwarning("Warning","Please enter a valid number!")
                    continue
                if bet_value>Balance:
                    tmsg.showwarning("Warning","Aukaat me reh!")
                    continue
                elif Bet==0:
                    if Balance>=initial_balance*2:
                        tmsg.showinfo("!Congratulations!","Malamal ho gaye Miya!")
                        break
                    elif Balance>=initial_balance*5:
                        tmsg.showinfo("!Congratulations!","paisa hi paisa hai Miya!")
                        break
                    elif Balance<initial_balance:
                        tmsg.showinfo("Game Over","Nuksaan ho gaya Miya!")
                        break
                else:
                    Balance-=Bet
                    tmsg.showinfo("!!Spinning!!")
                    num1=random.randint(1,10)
                    num2=random.randint(1,10)
                    num3=random.randint(1,10)
                    print("     <Result>")
                    print(f"| [{num1}] | [{num2}] | [{num3}] |")
                    if num1==num2==num3:
                        Balance=balance*5
                        tmsg.showinfo("Jackpot!","You won 5 times your bet!")
                    elif num1==num2 or num2==num3 or num1==num3:
                        Balance=balance*2
                        tmsg.showinfo("!Congratulations!","You won double your bet!")
                    tmsg.showinfo("Total amount",f"Total amount:{Balance}")
            else:
                tmsg.showinfo("Game Over","Lut gaye Miya!")
                break

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
#Ahh! This is hitting a extreme error, better see it tommorow!