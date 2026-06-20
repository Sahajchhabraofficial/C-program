from tkinter import *
from customtkinter import *

class TaskManager(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x1060")
        self.minsize(600,1060)
        self.title("Task Pro")

    def QuestLog(self):
        #Fonts
        Headings=CTkFont(family="Lucida",size=50,weight='bold',slant="roman")
        subheadings = CTkFont(family="Roboto",size=25,weight="normal",slant='roman')

        background_frame = CTkFrame(self,bg_color="transparent",fg_color="black",border_color="white",border_width=1)
        background_frame.pack(fill=BOTH,expand=True)

        #Profile bar
        Profile_bar = CTkFrame(background_frame,height=150,bg_color="transparent", fg_color="black", border_color="white",border_width=1)
        Profile_bar.pack(pady=5,padx=5,fill=X)

        # profile icon frame 
        profile_frame = CTkFrame(Profile_bar,height=150,width=150,bg_color="transparent", fg_color="black", border_color="white",border_width=1)
        profile_frame.pack(pady=12,padx=12,side=LEFT)

        #Username
        CTkLabel(Profile_bar,text="Sahaj Chhabra",font=Headings).pack(pady=5,padx=5)
        CTkLabel(Profile_bar,text="Rank name",font=CTkFont(family="Roboto",size=25,weight="normal",slant='italic'),bg_color="transparent").pack(pady=3,padx=5,side=LEFT)
        CTkLabel(Profile_bar,text="Level 14",font=subheadings).pack(pady=3,padx=5)

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