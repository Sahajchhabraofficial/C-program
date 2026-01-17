from tkinter import *
root=Tk()
root.title("Application")
#geometry of the window
root.geometry("400x500")
def enter():
    print(f"{name.get()}")
    with open("Data.txt","w") as filo:
        filo.write(f"{name.get()}\n")
Label(root,text="Hello!What is your name?",font=("comicsans",16,"bold")).pack()
name=Entry(root,width=30)
name.pack()
Button(root,text="Enter",font=("Serif",16,"bold"),command=enter).pack()

root.mainloop()