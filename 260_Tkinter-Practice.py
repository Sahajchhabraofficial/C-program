from tkinter import *
root=Tk()
root.title("Tkinter Practice")
#geometry of the window
root.geometry("400x500")
root.minsize(300,110)
#FRAME 1
f1=Frame(root,borderwidth=4,bg="Orange",relief=RAISED)
f1.pack(side="top",fill="x")
Label(f1,text="India",font=("Monospace",14,"bold"),fg="blue").pack()
#FRAME 2
f2=Frame(root,borderwidth=4,bg="white",relief=RAISED)
f2.pack(side="top",fill="x")
Label(f2,text="Is",font=("Monospace",14,"bold"),fg="blue").pack()
#FRAME 3
f3=Frame(root,borderwidth=4,bg="green",relief=RAISED)
f3.pack(side="top",fill="x")
Label(f3,text="Great",font=("Monospace",14,"bold"),fg="blue").pack()

root.mainloop()