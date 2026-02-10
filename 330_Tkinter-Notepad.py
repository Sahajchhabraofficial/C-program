from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tmsg
import os
root=Tk()
#geometry of the window
root.geometry("600x400")
root.minsize(600,400)
root.title("Notepad")
#all functions
def newfile():
    root.title("Untitled - Notepad")
    file=None
    Textarea.delete(1.0,END)
def openfile():
    file_path=filedialog.askopenfilename(title="select a file",filetypes=(("All files", "*.*"), ("Text files", "*.txt")))
    if file_path=="":
        file_path=None
    else:
        root.title(os.path.basename(file_path))
        Textarea.delete(1.0,END)
        fr=open(file_path,"r")
        Textarea.insert(1.0,fr.read())
        fr.close()
def savefile():
    try:
        file_path=filedialog.asksaveasfilename(title="save file",defaultextension=".txt",filetypes=(("All files", "*.*"), ("Text files", "*.txt")))
        if file_path=="":
            file_path=None
        else:
            content=Textarea.get(1.0,END)
            with open(file_path,"w") as fw:
                fw.write(content)
            tmsg.showinfo("Saved","file saved successfully")
    except Exception as e:
        tmsg.showerror("Error","an error occurred while saving: "+str(e))
def deletefile():
    try:
        confirmation=tmsg.askyesno("Delete","Are you sure you want to delete a file?")
        if confirmation:
            file_path=filedialog.askopenfilename(title="select a file to delete",filetypes=(("All files", "*.*"), ("Text files", "*.txt")))
            if file_path=="":
                file_path=None
            else:
                os.remove(file_path)
                tmsg.showinfo("Deleted","file deleted successfully")
        else:
            return
    except Exception as e:
        tmsg.showerror("Error","an error occurred while deleting: "+str(e))
def help():
    tmsg.showinfo("About","This is a notepad made by Sahaj chhabra, contact on 209347XXXX for more information")
def cut():
    Textarea.event_generate("<<Cut>>")
def copy():
    Textarea.event_generate("<<Copy>>")
def paste():
    Textarea.event_generate("<<Paste>>")
Textarea=Text(root,borderwidth=4,font="Helvatica 10")
Textarea.pack()
Statusbar=Menu(root)
File=Menu(Statusbar,tearoff=0)
File.add_command(label="New File",command=newfile)
File.add_command(label="Open File",command=openfile)
File.add_command(label="Save File",command=savefile)
File.add_command(label="Delete File",command=deletefile)
Edit=Menu(Statusbar,tearoff=0)
Edit.add_command(label="Cut",command=cut)
Edit.add_command(label="Copy",command=copy)
Edit.add_command(label="Paste",command=paste)
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