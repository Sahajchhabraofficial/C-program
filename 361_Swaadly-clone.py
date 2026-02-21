from tkinter import *
import customtkinter

root=customtkinter.CTk()
root.title("Swaadly-clone")
root.geometry("400x400")
#----- functions -----
def products():
    pass
#-----widgits-----

#Menubar
statusbar=Menu(root)
Ourproducts=Menu(statusbar,tearoff=0)
Ourproducts.add_command(label="Choclate crunchy",command=products)
Ourproducts.add_command(label="Creamy choclate",command=products)
Ourproducts.add_command(label="Classic Original",command=products)
statusbar.add_cascade(label="Our Products",menu=Ourproducts)
root.config(menu=statusbar)
Aboutus=Menu(statusbar,tearoff=0)
statusbar.add_cascade(label="About us",menu=Aboutus)
root.config(menu=statusbar)
AboutusFAQs=Menu(statusbar,tearoff=0)
statusbar.add_cascade(label="FAQ's",menu=AboutusFAQs)
root.config(menu=statusbar)

root.mainloop()

