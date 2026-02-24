from tkinter import *
import customtkinter
from PIL import Image, ImageTk


class Swaadly(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Swaadly-clone")
        self.geometry("600x400")

        self._create_menu()

    # ---- callbacks ----
    def products(self):
        print("Products clicked")

    def aboutus(self):
        print("About us clicked")

    def FAQs(self):
        print("FAQ clicked")

    # ---- UI construction helpers ----
    def _create_menu(self):
        menubar_frame = customtkinter.CTkFrame(self,bg_color="white",fg_color="white",border_width=0)
        menubar_frame.pack(side=TOP, fill=X, padx=8, pady=5)
        products=["Chocolate crunchy","Creamy Chocolate","Classic Original"]

        products_btn = customtkinter.CTkOptionMenu(menubar_frame,values=products,command=self.products, width=100,bg_color="white",fg_color="white",text_color="#FB9851",height=35,dropdown_fg_color="white",dropdown_text_color="#FB9851",dropdown_hover_color="#F5D3BB",button_color="white",button_hover_color="white")
        products_btn.pack(side=LEFT, padx=5)

        aboutus_btn = customtkinter.CTkButton(menubar_frame, text="About us", command=self.aboutus, width=100,hover_color="white",bg_color="white",fg_color="white",text_color="#FB9851",height=35)
        aboutus_btn.pack(side=LEFT, padx=5)

        faq_btn = customtkinter.CTkButton(menubar_frame, text="FAQ's", command=self.FAQs, width=100,hover_color="white",bg_color="white",fg_color="white",text_color="#FB9851",height=35)
        faq_btn.pack(side=LEFT, padx=5)
    def Homepage(self):
        frame=Frame(self,borderwidth=1)
        heading=Label(frame,text="Real Peanut Butter",font="Arial 16 bold")
        subheading=Label(frame,text="Made from premium peanuts. Slow roasted. Stone ground.",font="Arial 13")
        subheading2=Label(frame,text="No palm oil. No preservatives",font="Arial 13")
        frame.pack(expand=True,fill=BOTH)
        heading.pack(pady=5)
        subheading.pack(pady=4)
        subheading2.pack(pady=1)
        Learnmore=customtkinter.CTkButton(frame,
                                          text="Learn More >",
                                          corner_radius=50,
                                          width=5,
                                          hover_color="#CDCDCD",
                                          border_color="#000000",
                                          text_color="black",
                                          bg_color="white",
                                          fg_color="#ffffff",
                                          border_width=1)
        Learnmore.pack(pady=5,side=LEFT,padx=(185,5),anchor="n")
        Buynow=customtkinter.CTkButton(frame,
                                       text="   Buy Now   ",
                                       corner_radius=50,
                                       width=5,
                                       hover_color="#2A7D35",
                                       border_color="#000000",
                                       text_color="black",
                                       bg_color="white",
                                       fg_color="#00B218",
                                       border_width=1
        )
        Buynow.pack(pady=5,side=LEFT,padx=5,anchor="n")
        

if __name__ == "__main__":
    app = Swaadly()
    app.Homepage()
    app.mainloop()

