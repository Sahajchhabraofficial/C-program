from tkinter import *
import random
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk

# Main window
root = Tk()
root.title("Tkinter Casino")
root.geometry("1920x1080")
root.minsize(600, 400)


def get_started():
    start = Toplevel()  # Correct - using Toplevel
    start.title("Game selection")
    start.geometry("1920x1080")
    start_f1 = Frame(start, bg="white", relief="groove")
    start_f1.pack(pady=4)
    start_f2 = Frame(start, bg="white", relief="groove")
    start_f2.pack(pady=4)

    def start_game():
        game_window = Toplevel()  # Changed from Tk() to Toplevel()
        game_window.title("Jackpot 777")
        game_window.geometry("1920x1080")
        
        Label(game_window, text="What is your account balance?", 
              font=("Agency FB", 20, "bold"), bg="white").pack(pady=5)
        bal = Entry(game_window, font="Helvatica 14", bg="white", width=20)
        bal.pack(pady=5)
        
        Label(game_window, text="How much do you bet?", 
              font=("Agency FB", 20, "bold")).pack(pady=5)
        ent = Entry(game_window, width=20)
        ent.pack(pady=5)
        
        # Slot machine display frame
        slot_frame = Frame(game_window, bg="black", relief="ridge", bd=5)
        slot_frame.pack(pady=20)
        
        Label(slot_frame, text="🎰 SLOT MACHINE 🎰", font=("Impact", 20), 
              bg="black", fg="gold").pack(pady=10)
        
        # Container for the three reels
        reels_container = Frame(slot_frame, bg="black")
        reels_container.pack(pady=10, padx=20)
        
        # Create three slot reel displays
        slot1_frame = Frame(reels_container, bg="red", relief="raised", bd=5, width=100, height=120)
        slot1_frame.pack(side=LEFT, padx=5)
        slot1_frame.pack_propagate(False)
        slot1_label = Label(slot1_frame, text="?", font=("Arial Black", 48, "bold"), 
                           bg="white", fg="red")
        slot1_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        slot2_frame = Frame(reels_container, bg="red", relief="raised", bd=5, width=100, height=120)
        slot2_frame.pack(side=LEFT, padx=5)
        slot2_frame.pack_propagate(False)
        slot2_label = Label(slot2_frame, text="?", font=("Arial Black", 48, "bold"), 
                           bg="white", fg="blue")
        slot2_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        slot3_frame = Frame(reels_container, bg="red", relief="raised", bd=5, width=100, height=120)
        slot3_frame.pack(side=LEFT, padx=5)
        slot3_frame.pack_propagate(False)
        slot3_label = Label(slot3_frame, text="?", font=("Arial Black", 48, "bold"), 
                           bg="white", fg="green")
        slot3_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        # Result message label
        result_message = Label(slot_frame, text="Press PLAY to spin!", 
                              font=("Arial", 14, "bold"), bg="black", fg="yellow")
        result_message.pack(pady=10)
        
        balance_label = Label(game_window, text="", font=("Agency FB", 18, "bold"), 
                            fg="green")
        balance_label.pack(pady=5)

        def play_round():
            # Get values when button is clicked, not before
            balance_str = bal.get().strip()
            bet_str = ent.get().strip()
            
            # Validate balance
            if not balance_str:
                tmsg.showwarning("Warning", "Please enter your account balance!", parent=game_window)
                return
            
            try:
                balance = int(balance_str)
            except ValueError:
                tmsg.showwarning("Warning", "Please enter a valid balance!", parent=game_window)
                return
            
            if balance <= 0:
                tmsg.showwarning("Warning", "Balance must be greater than 0!", parent=game_window)
                return
            
            # Validate bet
            if not bet_str:
                tmsg.showwarning("Warning", "Please enter a bet amount!", parent=game_window)
                return
            
            try:
                bet = int(bet_str)
            except ValueError:
                tmsg.showwarning("Warning", "Please enter a valid bet amount!", parent=game_window)
                return
            
            if bet <= 0:
                tmsg.showwarning("Warning", "Bet must be greater than 0!", parent=game_window)
                return
            
            if bet > balance:
                tmsg.showwarning("Warning", "Aukaat me reh! (Bet cannot exceed balance)", parent=game_window)
                return
            
            # Store initial balance if not stored
            if not hasattr(play_round, 'initial_balance'):
                play_round.initial_balance = balance
                tmsg.showinfo("Warning", "--==Play at your own risk==--", parent=game_window)
            
            # Deduct bet
            balance -= bet
            
            # Spin the reels
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            num3 = random.randint(1, 10)
            
            # Display result on slot machine reels
            slot1_label.config(text=str(num1))
            slot2_label.config(text=str(num2))
            slot3_label.config(text=str(num3))
            
            # Check winnings
            if num1 == num2 == num3:
                winnings = bet * 5
                balance += winnings
                result_message.config(text="🎰 JACKPOT! 🎰 Triple Match!", fg="gold")
                tmsg.showinfo("🎰 JACKPOT! 🎰", f"You won 5 times your bet!\nWinnings: {winnings}", parent=game_window)
            elif num1 == num2 or num2 == num3 or num1 == num3:
                winnings = bet * 2
                balance += winnings
                result_message.config(text="🎉 WINNER! Double Match!", fg="lime")
                tmsg.showinfo("🎉 Winner! 🎉", f"You won double your bet!\nWinnings: {winnings}", parent=game_window)
            else:
                result_message.config(text="😢 No Match - Try Again!", fg="orange")
                tmsg.showinfo("😢 No Match", "Better luck next time!", parent=game_window)
            
            # Update balance display
            balance_label.config(text=f"Current Balance: {balance}")
            
            # Update the entry field
            bal.delete(0, END)
            bal.insert(0, str(balance))
            
            # Check game status
            if balance <= 0:
                tmsg.showinfo("💸 Game Over 💸", "Lut gaye Miya! You're out of money!", parent=game_window)
                game_window.destroy()
            elif balance >= play_round.initial_balance * 2:
                result = tmsg.askyesno("🏆 Great Success! 🏆", 
                                      f"Malamal ho gaye Miya!\nYou doubled your money!\n\nContinue playing?", parent=game_window)
                if not result:
                    game_window.destroy()
            elif balance >= play_round.initial_balance * 5:
                result = tmsg.askyesno("💰 Amazing! 💰", 
                                      f"Paisa hi paisa hai Miya!\nYou 5x'd your money!\n\nContinue playing?", parent=game_window)
                if not result:
                    game_window.destroy()

        def exit_game():
            if hasattr(play_round, 'initial_balance'):
                current_bal = bal.get().strip()
                if current_bal:
                    try:
                        final_balance = int(current_bal)
                        profit = final_balance - play_round.initial_balance
                        
                        if profit > 0:
                            message = f"Congratulations! 🎉\n\nStarting Balance: {play_round.initial_balance}\nFinal Balance: {final_balance}\nProfit: +{profit}\n\nGreat job!"
                        elif profit < 0:
                            message = f"Game Summary\n\nStarting Balance: {play_round.initial_balance}\nFinal Balance: {final_balance}\nLoss: {profit}\n\nBetter luck next time!"
                        else:
                            message = f"Game Summary\n\nStarting Balance: {play_round.initial_balance}\nFinal Balance: {final_balance}\nBreak Even!\n\nThanks for playing!"
                        
                        tmsg.showinfo("💰 Game Summary 💰", message, parent=game_window)
                    except:
                        pass
            
            game_window.destroy()

        # Buttons frame
        buttons_frame = Frame(game_window)
        buttons_frame.pack(pady=10)
        
        Button(buttons_frame, text="🎰 PLAY 🎰", font=("Agency FB", 15, "bold"), 
               command=play_round, bg="green", fg="white", width=15).pack(side=LEFT, padx=5, ipadx=10, ipady=5)
        
        Button(buttons_frame, text="💰 EXIT 💰", font=("Agency FB", 15, "bold"), 
               command=exit_game, bg="red", fg="white", width=15).pack(side=LEFT, padx=5, ipadx=10, ipady=5)

    Label(start_f1, text="Select your game please!", 
          font=("baskerville old face", 19, "bold"), bg="white").pack()
    
    Jackpot = Button(start_f2, text="Jackpot", font="Helvatica 14 italic", 
                     bg="white", command=start_game)
    Jackpot.grid(row=1, column=1, pady=5, padx=4)
    
    Coming_soon = Button(start_f2, text="Coming Soon", font="Helvatica 14 italic", 
                        bg="white", state=DISABLED)
    Coming_soon.grid(row=2, column=1, pady=5, padx=4)
    
    # Image loading with error handling
    try:
        Jackpot_imagePath = "C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\jackpot.jpg"
        Jackpot_image = Image.open(Jackpot_imagePath)
        Jackpot_image = Jackpot_image.resize((150, 150), Image.Resampling.LANCZOS)
        tk_Jackpot = ImageTk.PhotoImage(Jackpot_image)
        Jackpot_image_label = Label(start_f2, image=tk_Jackpot)
        Jackpot_image_label.image = tk_Jackpot
        Jackpot_image_label.grid(row=2, column=2, pady=5, padx=4)
    except Exception as e:
        print(f"Could not load jackpot image: {e}")
    
    try:
        Coming_soon_imagePath = "C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\Question mark.jpg"
        Coming_soon_image = Image.open(Coming_soon_imagePath)
        Coming_soon_image = Coming_soon_image.resize((150, 150), Image.Resampling.LANCZOS)
        tk_Coming_soon = ImageTk.PhotoImage(Coming_soon_image)
        Coming_soon_image_label = Label(start_f2, image=tk_Coming_soon)
        Coming_soon_image_label.image = tk_Coming_soon
        Coming_soon_image_label.grid(row=1, column=2, pady=5, padx=4)
    except Exception as e:
        print(f"Could not load question mark image: {e}")


# Main menu frame
frame = Frame(root, bg="white", relief="flat")
frame.pack(pady=350)

Label(frame, text="Welcome to Casino", bg="white", 
      font=("baskerville old face", 26, "bold"), fg="red").pack(pady=5, padx=5)

Label(frame,
      text="""Test your luck and sharpen your skills with our collection of classic casino games. 
      Place your bets, spin the wheels, and watch your virtual chips grow. 
      Remember - it's all about entertainment, so play responsibly and enjoy the excitement!""",
      font="Helvatica 14",
      fg="grey",
      bg="white"
      ).pack(pady=5, padx=5)

Button(frame, text="Get Started", font="Roboto 10 bold", height=1, 
       bg="white", command=get_started).pack(pady=5, ipady=5, ipadx=5, padx=5)

root.mainloop()