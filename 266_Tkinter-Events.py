from tkinter import *
root=Tk()
root.title("Events in tkinter")
root.geometry("400x500")
def hello(event):
    print(f"You clicked at coordinates ({event.x},{event.y})")
btn=Button(root,text="Button",font=("Agency FB",25,"bold"))
btn.bind("<Button-1>",hello)
btn.pack()

root.mainloop()