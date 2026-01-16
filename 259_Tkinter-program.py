from tkinter import *
root=Tk()
root.title("Practice")
#geomertry of the window
root.geometry("455x622")
#FRAME 1
def click():
    print("Button clicked!")
f1=Frame(root,borderwidth=4,bg="red",relief=SUNKEN)
f1.pack(side="top",fill="x")
Label(f1,text="Frame 1",font=("Arieal",14,"bold")).pack(pady=50)
Button(f1,text="Button",command=click).pack()

root.mainloop()