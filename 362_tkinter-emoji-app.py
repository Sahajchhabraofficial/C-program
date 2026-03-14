from tkinter import *
import customtkinter as ctk

# root=Tk()
# root.geometry("600x400")
# root.title("Emoji app")
# Label(root,text="🎉---Welcome to Emoji app---🎉",font=("Arial",15,"bold")).pack(pady=4)
# Button(root,text=" 💖 ",font="Arial 14 bold").pack(pady=4)

root=ctk.CTk()
root.geometry("400x400")
root.title("Emoji app")
label_font=ctk.CTkFont("Segoe UI", 24, "bold")
ctk.CTkLabel(master=root,text="🎉  🎉",font=label_font).pack(pady=4)

root.mainloop()