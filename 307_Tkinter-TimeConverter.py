#wap to convert specified seconds into years hours,minutes and seconds with a front-end design.
from tkinter import *
root=Tk()
root.title("Time converter")
root.geometry("400x500")
root.minsize(400,500)
def time():
    seconds=entry.get()
    hours=int(seconds/3600)
    seconds=seconds%3600
    minutes=int(seconds/60)
    seconds=seconds%60
    print("Hours: ",hours)
    print("Minutes: ",minutes)
    print("Seconds: ",seconds)
frame=Frame(root,borderwidth=5,relief=SUNKEN,bg="blue")
frame.pack(fill="x")
Label(frame,text="Enter the number of seconds please!",font=("Arial",14,)).pack(pady=10)
entry=Entry(frame,width=20)
entry.pack(pady=10)
Button(frame,text="Enter",font="Helvatica 14 bold",command=time).pack(pady=10)

root.mainloop()
#this program hits an error BRUAH!!