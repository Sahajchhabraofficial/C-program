from tkinter import *
root=Tk()
#geometry of window
root.geometry("490x339")
root.minsize(415,339)
#all functions
def click(event):
    shabd=val.get()
    if shabd!="Error":
        val.set(shabd+str(event))
    else:
        val.set("")
def calculate():
    try:
        scval=val.get()
        result=eval(scval)
        val.set(result)
    except Exception as error:
        val.set("Error")
#all frames
root.title("Calculator")
frame=Frame(root,borderwidth=5,relief="raised",bg="black")
entryframe=Frame(frame,borderwidth=5,relief="groove",bg="black")
entryframe.grid(row=1,column=1)
Allbtns=Frame(frame,borderwidth=5,relief="groove",bg="grey",width=400,height=400)
Allbtns.grid(row=2,column=1,sticky="w",padx=5)
frame.pack()
#variables
val=StringVar()
val.set("")
#all widgits
entry=Entry(entryframe,textvariable=val,width=14,font="Helvatica 45 bold")
entry.grid(row=1,column=1,pady=4)
#val=
Button(Allbtns,text="      1      ",font="Arial 20 bold",command=lambda:click(1)).grid(row=2,column=2)
Button(Allbtns,text="      2      ",font="Arial 20 bold",command=lambda:click(2)).grid(row=2,column=3)
Button(Allbtns,text="      3      ",font="Arial 20 bold",command=lambda:click(3)).grid(row=2,column=4)
Button(Allbtns,text="      4      ",font="Arial 20 bold",command=lambda:click(4)).grid(row=3,column=2)
Button(Allbtns,text="      5      ",font="Arial 20 bold",command=lambda:click(5)).grid(row=3,column=3)
Button(Allbtns,text="      6      ",font="Arial 20 bold",command=lambda:click(6)).grid(row=3,column=4)
Button(Allbtns,text="      7      ",font="Arial 20 bold",command=lambda:click(7)).grid(row=4,column=2)
Button(Allbtns,text="      8      ",font="Arial 20 bold",command=lambda:click(8)).grid(row=4,column=3)
Button(Allbtns,text="      9      ",font="Arial 20 bold",command=lambda:click(9)).grid(row=4,column=4)
Button(Allbtns,text="      0      ",font="Arial 20 bold",command=lambda:click(0)).grid(row=5,column=3)
Button(Allbtns,text="+",font="Arial 20 bold",command=lambda:click('+')).grid(row=2,column=1)
Button(Allbtns,text="-",font="Arial 20 bold",command=lambda:click('-')).grid(row=3,column=1)
Button(Allbtns,text="*",font="Arial 20 bold",command=lambda:click('*')).grid(row=4,column=1)
Button(Allbtns,text="/",font="Arial 20 bold",command=lambda:click('/')).grid(row=5,column=1)
Button(Allbtns,text="      C      ",font="Arial 20 bold",command=lambda:val.set("")).grid(row=5,column=4)
Button(Allbtns,text="      =      ",font="Arial 20 bold",command=lambda:calculate()).grid(row=5,column=2)

root.mainloop()