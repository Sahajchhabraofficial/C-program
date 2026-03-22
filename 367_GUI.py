from tkinter import *
import customtkinter as ctk
root= Tk()
root.geometry("600x400")
root.title("Sahaj GUI")

#--configuration--
Label_name="Ask from Gamma Bot!" 
Placeholder_name="Hey there!"
Button_name="Enter ➡️"
image_button=ctk.CTkFont(family="Segoe UI Emoji",weight="bold",slant="roman",underline=False,size=20)
image=ctk.CTkFont(family="Segoe UI Emoji",weight="bold",slant="roman",underline=False,size=85)
ctk.CTkLabel(master=root,
             text="🤖",
            #  width=50,
            #  height=120,
             text_color="black",
             font=image).pack(pady=4)
Font=ctk.CTkFont(family="Bookman Old Style",size=40,weight="bold",slant="roman")
ctk.CTkLabel(master=root,
             text=Label_name,
             text_color="#5B00FF",
             font=Font).pack(pady=4)
Input='''ctk.CTkInputDialog(fg_color="white",
                    text_color="black",
                    button_fg_color="pink",
                    button_hover_color="red",
                    button_text_color="white",
                    entry_fg_color="white",
                    entry_border_color="black",
                    entry_text_color="black",
                    title="hello",
                    font=Font,
                    text="Enter your name",
                    ).configure(pady=5)'''
# print(Input)
entry=ctk.CTkEntry(master=root,
                   width=225,
                   height=5,
                   corner_radius=8,
                   border_width=2,
                   bg_color="white",
                   text_color="black",
                   fg_color="white",
                   border_color="black",
                   placeholder_text=Placeholder_name,
                   placeholder_text_color="grey",
                   #font=Font,
                   state=NORMAL).pack(pady=5)
ctk.CTkButton(master=root,corner_radius=10,
              height=30,
              border_color="white",
              command=None,
              border_spacing=2,
              text=Button_name,
              text_color="white",
              fg_color="#FF00C8",
              bg_color="white",
              hover_color="#5B00FF",
              font=image_button,
              width=120,
              ).pack(pady=5,ipady=2)
root.mainloop()