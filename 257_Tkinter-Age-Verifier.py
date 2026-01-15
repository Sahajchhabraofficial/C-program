from tkinter import *
root=Tk()
root.title("Age Verifier")
label=Label(root,text="Enter your age",font=("Arial",16,"bold"))
label.pack()
#geometry of the window
root.geometry("500x400")
def clicked():
    age_text=int(entry.get())
    if age_text>=18:
        print("Jawan ho gaya tu pappe")
    elif age_text>=50:
        print("Buddhe! itna bhi nahi pata")
    else:
        print("Baccha hai tu abhi")
entry=Entry(root,width=30,font=("Arial",12))
entry.pack()
button=Button(root,text="Submit",font=("Monospace",14,"bold"),command=clicked)
button.pack()

root.mainloop()
#This Age verifer can detect age but you'll never see the output >D.