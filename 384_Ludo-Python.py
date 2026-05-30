#Ludo Game
from tkinter import *
from customtkinter import *
class Ludo(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.minsize(600,400)
        self.title("Ludo Python")

        # Fonts (create after the root window exists)
        self.Headings = CTkFont(family="Comic Sans MS", size=20, weight="bold")
        self.button_font = CTkFont(family="Impact", size=15, weight="normal", slant="roman")
        self.Score_font = CTkFont(family="Segoe UI", size=15, weight="normal", slant="roman")

        # Colors
        Red = "#ED0C0C"
        Green = "#3DEF10"
        Blue = "#1A13DD"
        Yellow = "#DFCA10"

    def Homepage(self):
        textbox = CTkTextbox(self, font=("Arial", 24, "bold"))
        textbox.pack(pady=2, padx=20)
        ludo_text="LUDO"
        textbox.insert("1.0",ludo_text)
        Ludo_colors = ["#ED0C0C", "#3DEF10", "#1A13DD", "#DFCA10"]
        for i, char in enumerate(ludo_text):
            tag_name = f"tag_{i}"
            start_index = f"1.{i}"
            end_index = f"1.{i+1}"
            color = Ludo_colors[i%len(Ludo_colors)]
            textbox.tag_config(tag_name, foreground=color)
            textbox.tag_add(tag_name, start_index, end_index)
        textbox.configure(state=DISABLED)
        textbox.insert("1","Python")

if __name__=="__main__":
    window = Ludo()
    window.Homepage()
    window.mainloop()