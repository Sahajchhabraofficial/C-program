from tkinter import *
root=Tk()
root.title("Application")
root.geometry("500x400")
Label(root,text="Enter your name",font=("Serif",14,"bold")).pack()
entry=Entry(root,width=40,font=("Arial",12,"italic"))
entry.pack()
def clicked():
    name=entry.get()
    print(name,"Boss")
Button(root,text="Enter",font=("comicsans",15,"bold"),bg="yellow",fg="blue",command=clicked).pack()

root.mainloop()
