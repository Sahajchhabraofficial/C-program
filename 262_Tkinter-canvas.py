from tkinter import *
root=Tk()
root.title("Canvas Practice")
canvas_width= 400
canvas_height= 500
can=Canvas(root,width=canvas_width,height=canvas_height,bg="light green")
can.pack(side="left")
can.create_line(0,0,400,500)
can.create_arc(150,195,250,295,start=75,extent=75,fill="blue")
can.create_text(200,250,text="Text of Tkinter Canvas",font=("Agency FB",18,"bold"))

root.mainloop() 