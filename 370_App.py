from tkinter import *
import customtkinter as ctk

class StreamPro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("🎧 Stream Pro")
        self.minsize(600,400)

    def User_Profile(self):
        print("User profile clicked")

    def HomePage(self):
        Emoji_font=ctk.CTkFont(family="Seoge UI Emoji",
                               size=30,
                               weight="normal",
                               slant="roman")
        Emoji_font_cstm=ctk.CTkFont(family="Seoge UI Emoji",
                               size=25,
                               weight="normal",
                               slant="roman")
        Side_Frame=ctk.CTkFrame(master=self,
                         bg_color='black',
                         fg_color="#242424",
                         corner_radius=10,
                         border_color="white",
                         border_width=1)
        Side_Frame.pack(pady=5,side=LEFT,fill=Y)
        PlayBack_Frame=ctk.CTkFrame(master=self,
                                     bg_color='black',
                                     fg_color="#242424",
                                     corner_radius=10,
                                     border_color='white',
                                     border_width=1)
        PlayBack_Frame.pack(pady=4,side=BOTTOM,fill=X)
        Label(master=self,
              text="🎧",
              font=("Seoge UI Emoji",30,"bold")).pack(pady=4)
        Label(master=self,
              text="Welcome to Stream Pro",
              font="Arial 16 bold").pack(pady=5)
        Songs_Frame=ctk.CTkScrollableFrame(master=self,
                                           bg_color='black',
                                            fg_color="#242424",
                                            corner_radius=10,
                                            border_color='white',
                                            border_width=1,
                                            orientation='horizontal',
                                            width=275,
                                            label_text="Untitled Album",)
        Songs_Frame.pack(pady=4)
        
        for i in range(5):
            Song=ctk.CTkFrame(master=Songs_Frame,
                                width=150,
                                height=150,
                                corner_radius=5,
                                border_width=1,
                                border_color="white",
                                )
            image=Frame(master=Song,
                        background="#224AFF",
                        width=100,
                        height=97)
            image.pack(pady=8,padx=8)
            Label(master=Song,
                  text=f"Song - {i+1}",
                  background="black",
                  foreground="white").pack(pady=3)
            # ctk.CTkLabel(master=Song,
            #       text="Unkown artist",
            #       text_color="white"
            #       ).pack(pady=2)
            Song.pack(pady=3,padx=2,side=LEFT)
        PlayPause_icon=ctk.CTkButton(master=PlayBack_Frame,
                                   text="    ▶️",
                                   width=30,
                                   font=Emoji_font_cstm,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   hover=TRUE,
                                   hover_color="#8F8D8D",
                                   command=lambda:self.User_Profile())
        PlayPause_icon.grid(row=1,column=2)
        Previous_icon=ctk.CTkButton(master=PlayBack_Frame,
                                   text="⏮️",
                                   width=30,
                                   font=Emoji_font_cstm,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   hover=TRUE,
                                   hover_color="#8F8D8D",
                                   command=lambda:self.User_Profile())
        Previous_icon.grid(row=1,column=1,padx=(95,0))
        Next_icon=ctk.CTkButton(master=PlayBack_Frame,
                                   text="⏭️",
                                   width=30,
                                   font=Emoji_font_cstm,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   hover=TRUE,
                                   hover_color="#040404",
                                   command=lambda:self.User_Profile())
        Next_icon.grid(row=1,column=3)
        TimeLine_icon=ctk.CTkSlider(master=PlayBack_Frame,
                                    width=250,
                                    height=17,
                                    corner_radius=5,
                                    button_color="green",
                                    button_corner_radius=5,
                                    border_width=2,
                                    button_length=5)
        TimeLine_icon.grid(row=2,column=2,pady=5)
        Profile_icon=ctk.CTkButton(master=Side_Frame,
                                   text="🥸",
                                   width=45,
                                   height=60,
                                   font=Emoji_font,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   hover=TRUE,
                                   corner_radius=2,
                                   hover_color="#8F8D8D",
                                   command=lambda:self.User_Profile())
        Profile_icon.pack(padx=2,pady=3)
        More_actions=ctk.CTkButton(master=Side_Frame,
                                   text="•••",
                                   width=45,
                                   height=60,
                                   font=Emoji_font,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   hover=TRUE,
                                   hover_color="#8F8D8D",
                                   command=lambda:self.User_Profile())
        More_actions.pack(padx=2,pady=3)
        Settings_icon=ctk.CTkButton(master=Side_Frame,
                                   text="⚙️",
                                   width=45,
                                   height=60,
                                   font=Emoji_font,
                                   bg_color="white",
                                   fg_color="white",
                                   text_color="black",
                                   hover=TRUE,
                                   hover_color="#8F8D8D",
                                   command=lambda:self.User_Profile())
        Settings_icon.pack(padx=3,pady=3,side=BOTTOM)
        
    def User_Profile():
        print("User profile clicked")

if __name__=="__main__":
    Application=StreamPro()
    Application.HomePage()
    Application.mainloop()
