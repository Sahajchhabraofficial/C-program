#wap to swap two values of two variables with front-end.
from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("Number swapper")
frame=Frame(root,borderwidth=5,bg="orange",relief=GROOVE)
frame.pack(fill="x",pady=150)
Label(frame,text="enter first number:",font="Helvatica 14 bold").grid(row=1,columns=1,pady=5)
Label(frame,text="enter second number:",font="Helvatica 14 bold").grid(row=2,columns=1,pady=5)
entry1=Entry(frame,width=20)
entry1.grid(row=1,column=2,padx=7)
entry2=Entry(frame,width=20)
entry2.grid(row=2,column=2,padx=7)

root.mainloop()