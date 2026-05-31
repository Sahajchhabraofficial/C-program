#Ludo Game
from tkinter import *
from customtkinter import *
from PIL import Image
import os
class Ludo(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.minsize(600,910)
        self.title("Ludo Python")

        # Fonts (create after the root window exists)
        self.Headings = CTkFont(family="Comic Sans MS", size=20, weight="bold")
        self.button_font = CTkFont(family="Impact", size=25, weight="normal", slant="roman")
        self.Score_font = CTkFont(family="Segoe UI", size=15, weight="normal", slant="roman")

        # Colors
        Red = "#ED0C0C"
        Green = "#3DEF10"
        Blue = "#1A13DD"
        Yellow = "#DFCA10"

    def Homepage(self):
        # textbox = CTkTextbox(self, font=("Arial", 24, "bold"))
        # textbox.pack(pady=2, padx=20)
        # ludo_text="LUDO"
        # textbox.insert("1.0",ludo_text)
        # Ludo_colors = ["#ED0C0C", "#3DEF10", "#1A13DD", "#DFCA10"]
        # for i, char in enumerate(ludo_text):
        #     tag_name = f"tag_{i}"
        #     start_index = f"1.{i}"
        #     end_index = f"1.{i+1}"
        #     color = Ludo_colors[i%len(Ludo_colors)]
        #     textbox.tag_config(tag_name, foreground=color)
        #     textbox.tag_add(tag_name, start_index, end_index)
        # textbox.configure(state=DISABLED)

        frame = CTkFrame(self,bg_color="transparent",fg_color="black",border_width=1,border_color="white")
        frame.pack(expand=True,fill=BOTH)
    
        Title = CTkFrame(frame,fg_color="black",border_width=1,border_color="white")
        Title.pack(pady=7)
        L = Frame(Title,bg="Red")
        L.pack(side=LEFT,pady=5,padx=2)
        CTkLabel(L,text="L",font=self.Headings,bg_color="transparent",text_color="white").pack(pady=10,padx=7)
        U = Frame(Title,bg="Green")
        U.pack(side=LEFT,pady=5,padx=2)
        CTkLabel(U,text="U",font=self.Headings,bg_color="transparent",text_color="white").pack(pady=10,padx=7)
        D = Frame(Title,bg="Blue")
        D.pack(side=LEFT,pady=5,padx=2)
        CTkLabel(D,text="D",font=self.Headings,bg_color="transparent",text_color="white").pack(pady=10,padx=7)
        O = Frame(Title,bg="Yellow")
        O.pack(side=LEFT,pady=5,padx=2)
        CTkLabel(O,text="O",font=self.Headings,bg_color="transparent",text_color="white").pack(pady=10,padx=7)
        CTkLabel(Title,text="Python",font=self.Headings).pack(padx=4,pady=12)
        CTkLabel(frame,text="Try the classic ludo in python version 🐍",font=self.Score_font).pack(pady=5,padx=5)

        # Load and display the Ludo image
        image_path = os.path.join(os.path.dirname(__file__), "ludo.jpg")
        if os.path.exists(image_path):
            ludo_image = CTkImage(light_image=Image.open(image_path), size=(300, 200))
            image_label = CTkLabel(frame, image=ludo_image, text="")
            image_label.image = ludo_image  # Keep a reference
            image_label.pack(pady=15)

        CTkButton(frame,
                  text="Play",
                  corner_radius=10,
                  border_color="white",
                  border_width=1,
                  font=self.button_font).pack(pady=5,padx=5)
        

if __name__=="__main__":
    window = Ludo()
    window.Homepage()
    window.mainloop()