from tkinter import *
root=Tk()
root.title("Tkinter Menubars")
root.geometry("400x600")
#all functions
def Newfile():
    print("Welcome to new file")
def Openfile():
    print("File opened")
def Savefile():
    print("File saved")
def Deletefile():
    print("File deleted")
Main=Menu(root)
option1=Menu(Main,tearoff=0)
option1.add_command(label="New File",command=Newfile)
option1.add_command(label="Open File",command=Openfile)
option1.add_command(label="Save File",command=Savefile)
option1.add_command(label="Delete File",command=Deletefile)
option1.add_separator()
option1.add_command(label="Exit",command=root.quit)
Main.add_cascade(label="File",menu=option1)
root.config(menu=Main)

root.mainloop()