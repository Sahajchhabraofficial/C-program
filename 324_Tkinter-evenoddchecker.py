from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("400x400")
root.title("Even-Odd Checker")
root.minsize(400,400)
def check():
    num=int(entry.get())
    if num%2==0:
        tmsg.showinfo("Result","Number is Even!")
    else:
        tmsg.showinfo("Result","Number is Odd!")
frame=Frame(root,borderwidth=5,relief=GROOVE,bg="green")
frame.pack(pady=100)
Label(frame,text="Enter a number",font="Comicsans 16 bold").pack(pady=4,padx=7)
entry=Entry(frame,width=20)
entry.pack(pady=4,padx=7)
Button(frame,text="Submit",font="Arial 10 bold",command=check).pack(pady=4,padx=7)


root.mainloop()