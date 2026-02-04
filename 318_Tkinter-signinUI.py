from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Sign-in Startup")
root.minsize(600, 300)

# Main Frame
frame = Frame(root, borderwidth=5, relief=RAISED)
frame.pack(pady=20)

# Load Image
limg = PhotoImage(file="C:/Users/LOQ/Downloads/Friendly Smile Against Vibrant Gradient.png")

# Image Label
img_label = Label(frame, image=limg)
img_label.pack(pady=10)

# Text Label
text_label = Label(
    frame,
    text="Sign-in to access content",
    font="Arial 15 bold"
)
text_label.pack(pady=10)

root.mainloop()
