#wap to swap two values of two variables with front-end.
from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("Number swapper")
def process():
    num1=entry1.get()
    num2=entry2.get()
    temp=num1
    num1=num2
    num2=temp
    win=Tk()
    win.geometry("600x400")
    win.title("Swapped numbers!")
    Numframes=Frame(win,borderwidth=5,bg="red",relief=RAISED)
    Numframes.pack(fill="x")
    lab1=Label(Numframes,text="Value of first number",font="Arieal 14 bold")
    val1=Label(Numframes,text=f"{num1}",font="AgencyFB 15 bold")
    lab2=Label(Numframes,text="Value of second number",font="Arial 14 bold")
    val2=Label(Numframes,text=f"{num2}",font="AgencyFB 15 bold")
    lab1.pack()
    val1.pack()
    lab2.pack()
    val2.pack()
    win.mainloop()
frame=Frame(root,borderwidth=5,bg="orange",relief=GROOVE)
frame.pack(fill="x",pady=150)
Label(frame,text="enter first number:",font="Helvatica 14 bold").grid(row=1,columns=1,pady=5)
Label(frame,text="enter second number:",font="Helvatica 14 bold").grid(row=2,columns=1,pady=5)
entry1=Entry(frame,width=20)
entry1.grid(row=1,column=2,padx=7)
entry2=Entry(frame,width=20)
entry2.grid(row=2,column=2,padx=7)
Button(frame,text="Enter",font="Helvatica 16 bold",command=process).grid(row=3,columns=3,pady=5)

root.mainloop()