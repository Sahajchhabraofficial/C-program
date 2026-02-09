from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tmsg
root=Tk()
#geometry of the window
root.geometry("400x400")
root.minsize(600,400)
root.title("Notepad")
#all functions
def newfile():
    new=Tk()
    new.title("Untitled file")
    new.mainloop()
def openfile():
    file_path=filedialog.askopenfilename(title="select a file",filetypes=(("All files", "*.*"), ("Text files", "*.txt")))
    if file_path:
        with open(file_path,'r') as f:
            content=f.read()
            
        #print("file opened: ",file_path)
def savefile():
    pass
def deletefile():
    pass
def help():
    pass
Statusbar=Menu(root)
File=Menu(Statusbar,tearoff=0)
File.add_command(label="New File",command=newfile)
File.add_command(label="Open File",command=openfile)
File.add_command(label="Save File",command=savefile)
File.add_command(label="Delete File",command=deletefile)
Edit=Menu(Statusbar,tearoff=0)
Edit.add_command(label="Cut")
Edit.add_command(label="Copy")
Edit.add_command(label="Paste")
View=Menu(Statusbar,tearoff=0)
View.add_command(label="Zoom In")
View.add_command(label="Zoom Out")
Help=Menu(Statusbar,tearoff=0)
Help.add_command(label="About",command=help)
Statusbar.add_cascade(label="File",menu=File)
Statusbar.add_cascade(label="Edit",menu=Edit)
Statusbar.add_cascade(label="View",menu=View)
Statusbar.add_cascade(label="Help",menu=Help)
root.config(menu=Statusbar)

root.mainloop()