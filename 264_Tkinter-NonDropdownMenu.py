from tkinter import *
root=Tk()
root.title("Tkinter Non-dropdown Menubars")
root.geometry("500x350")
#functions
def Dunc():
    print("options triggered")
Mainmenu=Menu(root)
Mainmenu.add_command(label="Options",command=Dunc)
Mainmenu.add_command(label="Exit",command=quit)
root.config(menu=Mainmenu)

root.mainloop()