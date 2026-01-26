from tkinter import *
class oops(Tk):
    def __init__(self):
        super().__init__()  
        self.geometry("400x500")
        self.title("OOPs in tkinter")
        self.minsize(400,500)

    def status(self):
        self.var=StringVar()
        self.var.set("Stauts Bar")
        self.statusbar=Label(self,textvar=self.var,relief=SOLID,anchor='w',borderwidth=5)
        self.statusbar.pack(side=BOTTOM,fill=X)
if __name__=="__main__":
    mywin=oops()
    mywin.status()
    mywin.mainloop()