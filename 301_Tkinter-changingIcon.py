from tkinter import *
root=Tk()
root.geometry("650x500")
root.title("<---Car Icon")
#root.wm_iconbitmap("Car_icon-removebg-preview.ico")
icon=PhotoImage(file="Car icon.png")
root.iconphoto(True,icon)
Label(root,text="This window has a custom icon :)",font=("Elephant",18,"bold")).pack()

root.mainloop()