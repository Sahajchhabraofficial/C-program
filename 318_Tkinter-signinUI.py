from tkinter import *
import tkinter.messagebox as tmsg
import csv

root = Tk()
root.geometry("600x400")
root.title("Sign-in Startup")
root.minsize(600, 300)

def Check_email(Email):
    Email=str(Email)
    with open("C-program/Data.csv",mode='r',newline='') as datafile:
        username=csv.reader(datafile,delimiter=',')
        for name in username:
            if Email==name[0]:
                return True
        else:
            return False
            

def Check_password(Password):
    Password=str(Password)
    with open("C-program/Data.csv",mode='r') as datafile:
        username=csv.reader(datafile,delimiter=',')
        for name in username:
            if Password==name[1]:
                return True
        else:
            return False

def submit():
    if Check_email(Ementry):
        if Check_password(Pasentry):
            tmsg.showinfo("Access Granted!","You have now permission to access the content")
        else:
            tmsg.showerror("Access Denied!","Double check you password")
    else:
        tmsg.showerror("Access Denied!","You don't have permission to access content")

# Main Frame
frame = Frame(root, borderwidth=5, relief=RAISED)
frame.pack(pady=20)

# Load Image
limg = PhotoImage(file="C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\Friendly Smile Against Vibrant Gradient.png")

# Resizing the image
limg=limg.subsample(4, 4)

# Image Label
img_label = Label(frame, image=limg)
img_label.pack(pady=10)

# Text Label
text_label = Label(
    frame,
    text="Sign-in to access content",
    font="Arial 15 bold"
)
text_label.pack(pady=5)

# Email Label
E_label= Label(
    frame,
    text="Enter your email",
    font="Arial 15 bold"
).pack(pady=5)

# E-mail Entry
Ementry=Entry(
    frame,
    width=40
)
Ementry.pack(pady=5)

# Email Label
E_label= Label(
    frame,
    text="Enter your password",
    font="Arial 15 bold"
).pack(pady=5)

# Password show button
pass_btn=Button(
    frame,
    text="👁"
).pack(side=RIGHT,anchor="n",ipadx=0,ipady=0)

# Password Entry
Pasentry=Entry(
    frame,
    width=40
)
Pasentry.pack(pady=5)

# Submit Button
Submit= Button(
    frame,
    text="Submit",
    font="Arial 15 bold",
    command=submit
).pack(pady=5)

root.mainloop()
