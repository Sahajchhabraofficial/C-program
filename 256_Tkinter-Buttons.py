from tkinter import *
root=Tk()
root.title("Buttons in Tkinter")
sign=Label(root,text="Enter Hello!",font=("Arial",16,"bold"))
sign.pack()
#geometry of the window
root.geometry("500x400")
def clicked():
    text=entry.get()
    if text=="Hello":
        print("Do your work")
    else:
        print("Bruah!")
entry=Entry(root,width=30)
entry.pack()
button=Button(root,text="Submit",command=clicked,bg="red",fg="lightgreen",font=("Monospace",14,"bold"))
button.pack()

root.mainloop()
