from tkinter import *
from customtkinter import *

class TaskManager(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x1060")
        self.minsize(600,1060)
        self.title("Task Pro")

    def QuestLog(self):
        background_frame = CTkFrame(self,bg_color="transparent",fg_color="black",border_color="white",border_width=1)
        background_frame.pack(fill=BOTH,expand=True)

        #Username bar
        Username_bar = CTkFrame(background_frame,height=150,bg_color="transparent", fg_color="black", border_color="white",border_width=1)
        Username_bar.pack(pady=5,padx=5,fill=X)

        # profile icon frame 
        profile_frame = CTkFrame(background_frame,height=550,bg_color="transparent", fg_color="black", border_color="white",border_width=1)
        profile_frame.pack(pady=5,padx=12,fill=X)

        slider = CTkProgressBar(background_frame,width=100,height=15,corner_radius=8)
        slider.pack()

    def Inventory(self):
        pass

    def LeaderBoard(self):
        pass

    def Profile(self):
        pass


if __name__ == "__main__":
    first_window = TaskManager()
    first_window.QuestLog()
    first_window.mainloop() 