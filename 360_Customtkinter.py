import customtkinter
import tkinter as tk
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk
root=customtkinter.CTk()
root.geometry("600x400")
root.title("Custom tkinter lib")
#----- functions ------
def settings():
    tmsg.showinfo("Info","Coming Soon")

def start():
    tmsg.showinfo("Hello","This is customized version of tkinter library in python")

# ----- widgits -----
#image
image_path=Image.open("C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\settings.png").resize((70,60))
settings_image=ImageTk.PhotoImage(image_path)
#font   
label_font=customtkinter.CTkFont(family="Agency FB",size=50,weight="normal")
button_font=customtkinter.CTkFont(family="Helvatica",size=15,weight="bold",slant="italic")
#label
label=customtkinter.CTkLabel(
    master=root,
    text="Welcome to custom tkinter!",
    width=50,
    height=100,
    text_color="#22FF00",
    font=label_font
)
label.pack(pady=5)
#button
button=customtkinter.CTkButton(
master=root,
text="Start >",
text_color="#000000",
bg_color="#000000",
fg_color="#FFFCFC",
hover_color="#22FF00",
border_width=2,
corner_radius=20,
font=button_font,
border_color="#000000",
command=start
)
button.pack(pady=9)
#settings button
# use the PhotoImage instance for the button, not the PIL image
settings=tk.Button(master=root,
    text="",
    image=settings_image,
    bd=0,
    compound="center",
    command=settings
    )
# keep a reference to prevent garbage collection
settings.image = settings_image
settings.pack(pady=90,ipadx=7,ipady=7)

root.mainloop()