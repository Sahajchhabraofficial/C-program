import tkinter as tk
root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300")
label = tk.Label(root,text="Welcome To age Verifier")
label.pack()
entry=tk.Entry(root,width=30)
text=entry.get()
entry.pack()
def clicked():
    print("Button clicked")
button=tk.Button(root,text="Enter",command=clicked)
button.pack()
root.mainloop()
#This Aage verifier GUI program never works cuz i am learning yet.