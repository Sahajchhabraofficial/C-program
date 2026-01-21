from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("Age Verifier")
root.geometry("600x400")
def verify_age():
    age=entry.get()
    if age.isdigit()==True:
        age=int(age)
        if age>=50 and age<70:
            tmsg.showinfo("Result","Buddhe! itna bhi nahi pata")
        elif age>=18 and age<50:
            tmsg.showinfo("Result","Jawan ho gaya tu pappe")
        elif age>=70 and age<=100:
            tmsg.showinfo("Result","Rehne do chacha kya kroge vote dekar,tapakne wale ho jaldi")
        elif age>=100:
            tmsg.showinfo("Result","Chal chal jyada feek mat, chupchaap sahi age daal")
        else:
            tmsg.showinfo("Result","Baccha hai tu abhi")
    else:
        tmsg.showinfo("Result","Oh! mahagyani insaan age daal chupchaap")
frame=Frame(root,borderwidth=5,relief=RAISED,bg="orange")
frame.pack(pady=400)
Label(frame,text="Enter your age, please!",font=("Agency FB",18,"bold")).pack(pady=10,padx=100)
entry=Entry(frame,width=15,font=("Arial",18,"italic"))
entry.pack(pady=10,padx=100)
Button(frame,text="Enter",font=("Helvatica",16,"bold"),command=verify_age).pack(pady=10,padx=100)

root.mainloop()