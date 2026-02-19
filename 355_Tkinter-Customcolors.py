from tkinter import *
root=Tk()
root.title("Custom colors in tkinter")
root.geometry("600x400")
Orange="#DE7B50"
White="#FFFFFF"
Green="#47C34D"
Orange_frame=Frame(root,relief="raised",borderwidth=5,bg=Orange)
White_frame=Frame(root,relief="raised",borderwidth=5,bg=White)
Green_frame=Frame(root,relief="raised",borderwidth=5,bg=Green)
Orange_frame.pack(fill="x")
White_frame.pack(fill="x")
Green_frame.pack(fill="x")
Label(Orange_frame,text="India",font=("Calisto MT",18,"bold"),bg=Orange,fg="blue").pack(pady=5)
Label(White_frame,text="is",font=("Calisto MT",18,"bold"),bg=White,fg="blue").pack(pady=5)
Label(Green_frame,text="Great",font=("Calisto MT",18,"bold"),bg=Green,fg="blue").pack(pady=5)

root.mainloop()