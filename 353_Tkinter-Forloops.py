from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("Forloops in tkinter")
for i in range(3):
    Label(root,text=f"This is label {i}",font="Helvatica 16").pack(pady=5)
Entry(root,width=30).pack(pady=5)

root.mainloop()