from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Messsage boxes in tkinter")
root.geometry("500x350")
root.minsize(325,250)
def Message():
    print("Messages")
    tmsg.showinfo("Information","This is information message box")
def Information():
    print("More Information")
    value=tmsg.askquestion("Question","Do you like Python?")
    print(value)
    if value=='yes':
        tmsg.showinfo("Response","You clicked yes")
    else:
        tmsg.showinfo("Response","You clicked no") 
menu=Menu(root)
menu.add_command(label="Show Info",command=Message)
menu.add_command(label="Exit",command=root.quit)
menu.add_command(label="info",command=Information)
root.config(menu=menu)

root.mainloop()