from tkinter import *
root=Tk()
root.title("Tkinter Frames")
#geoemetry of the window
root.geometry("500x400")
root.minsize(500,400)
#FRAME 2
f2=Frame(root,bg="blue",borderwidth=4,relief=SOLID)
f2.pack(side="bottom",fill="x")
label2=Label(f2,text="Tkinter Frame 2",font=("Helvatica",16,"bold"))
label2.pack(pady=2)
#FRAME 1
f1=Frame(root,bg="blue",borderwidth=5,relief=SOLID)
f1.pack(side=LEFT,fill='y')
label=Label(f1,text="Tkinter Frame 1",font=("Serif",12,))
label.pack(pady=140,fill="y")
#FRAME 3
f3=Frame(root,bg="blue",borderwidth=4,relief=SOLID)
f3.pack(side="right",fill="y")
label3=Label(f3,text="Tkinter Frame 3",font=("Arial",14,"italic"))
label3.pack(pady=140,fill="y")
#FRAME 4
f4=Frame(root,bg="blue",borderwidth=4,relief=SOLID)
f4.pack(side="top",fill="x")
Label4=Label(f4,text="Tkinter Frame 4",font=("Monospace",14,"bold"))
Label4.pack(pady=2)

root.mainloop()