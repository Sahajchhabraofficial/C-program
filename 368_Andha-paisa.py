from tkinter import *
import customtkinter as ctk
from tkinter import messagebox as tmsg

root=Tk()
root.geometry("600x400")
root.title("Andha paisa")
label_font=ctk.CTkFont(family="Josefin Sans",size=25,slant="roman",weight="bold")
button_font=ctk.CTkFont(family="Parabolica",size=20,slant="roman",weight="bold")
heading_font=ctk.CTkFont(family="Monotalic",size=30,slant="roman",weight="bold")
subheading_font=ctk.CTkFont(family="Monotalic",size=15,slant="roman",weight="normal")
def Haan():
    root2=Toplevel()
    root2.title("Welcome berozgaar admi")
    root2.geometry("600x400")
    ctk.CTkLabel(master=root2,
             text="So welcome to",
             text_color="black",
             font=subheading_font
             ).pack(pady=4)
    ctk.CTkLabel(master=root2,
             text="Paisa Chaapne ki macine",
             text_color="black",
             font=heading_font
             ).pack(pady=4)
    ctk.CTkLabel(master=root2,
             text="Boliye kina paisa chahiye aapko?",
             text_color="black",
             font=subheading_font
             ).pack(pady=4)
    amount=ctk.CTkEntry(master=root2,
                 width=140,
                 bg_color="white",
                 fg_color="white",
                 border_color="black",
                 border_width=3,
                 placeholder_text="Eg.10000",
                 text_color="black",
                 placeholder_text_color="grey")
    
    def check_amount():
        try:
            amount_value = int(amount.get())
            if amount_value >= 100000:
                tmsg.showinfo("Paisa hi Paisa!", f"Aap Ameer ho gay!! Bank Amount = ₹{amount_value}")
            else:
                tmsg.showinfo("Gareebi", f"Rehne de bhai! ₹{amount_value} ki choclate khale jaa ke")
        except ValueError:
            tmsg.showerror("Error", "Kripya ek valid sankhya enter karein!")

    amount.pack(pady=4)
    ctk.CTkButton(master=root2,
                  text="Enter",
                  text_color="black",
                  hover_color="light green",
                  corner_radius=5,
                  bg_color="white",
                  fg_color="yellow",
                  command=check_amount).pack(pady=4)
    
    if int(amount)>=100000:
        tmsg.showinfo("Paisa hi Paisa!",f"Aap Ameer ho gay!! Bank Amount = ₹{int(amount)}")
    else:
        tmsg.showinfo("Gareebi",f"Rehne de bhai! ₹{int(amount)} ki choclate khale jaa ke")

    root2.mainloop()
def Naa():
    tmsg.showinfo("Not for you!","Toh jaa ke apna kaam karo, yaha kyu timepaas kar rahe ho")
ctk.CTkLabel(master=root,
             text="Kya aap berozgaar hain?",
             text_color="black",
             font=label_font
             ).pack(pady=4)
ctk.CTkButton(master=root,
              text="Haan",
              text_color="black",
              corner_radius=6,
              bg_color="white",
              fg_color="yellow",
              font=button_font,
              hover=True,
              command=Haan,
              hover_color="light green").pack(pady=4)
ctk.CTkButton(master=root,
              text="Na",
              text_color="black",
              corner_radius=6,
              bg_color="white",
              fg_color="yellow",
              font=button_font,
              hover=True,
              command=Naa,
              hover_color="light green").pack(pady=4)

root.mainloop()