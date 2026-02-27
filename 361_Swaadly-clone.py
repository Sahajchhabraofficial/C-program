from tkinter import *
import customtkinter
from PIL import Image, ImageTk


class Swaadly(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Swaadly-clone")
        self.geometry("600x400")

        self._create_menu()

    # ---- Menubar callbacks ----
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

        options_menu_font=customtkinter.CTkFont(family="Segoe UI",size=15)

        swaadly_logo_path="c:\\Users\\LOQ\\OneDrive\\Pictures\\Screenshots\\Screenshot 2026-02-27 130930.png"
        swaadly_logo=Image.open(swaadly_logo_path)
        swaadly_logo=ImageTk.PhotoImage(swaadly_logo)

        swaadly_logo_button=customtkinter.CTkButton(menubar_frame,image=swaadly_logo,
                                                    text="",
                                                    fg_color="white",
                                                    bg_color="white",
                                                    hover_color="white",
                                                    command=self.Homepage,
                                                    height=1)
        swaadly_logo_button.pack(pady=(2,6),padx=2,side=LEFT)

        products=["Chocolate crunchy","Creamy Chocolate","Classic Original"]
        text=StringVar(value="Our Produts")
        products_btn = customtkinter.CTkOptionMenu(menubar_frame,
                                                   values=products,
                                                   command=lambda v: self.products(),
                                                   width=100,
                                                   font=options_menu_font,
                                                   variable=text,
                                                   bg_color="white",
                                                   fg_color="white",
                                                   text_color="#C48B4D",
                                                   height=35,
                                                   dropdown_fg_color="white",
                                                   dropdown_text_color="#C48B4D",
                                                   dropdown_hover_color="#F5D3BB",
                                                   button_color="white",
                                                   button_hover_color="white")
        products_btn.pack(side=LEFT, padx=5)

        aboutus_btn = customtkinter.CTkButton(menubar_frame, text="About us", font=options_menu_font,command=self.aboutus, width=100,hover_color="white",bg_color="white",fg_color="white",text_color="#C48B4D",height=35)
        aboutus_btn.pack(side=LEFT, padx=5,ipadx=1,ipady=1)

        faq_btn = customtkinter.CTkButton(menubar_frame, text="FAQ's", font=options_menu_font,command=self.FAQs, width=100,hover_color="white",bg_color="white",fg_color="white",text_color="#C48B4D",height=35)
        faq_btn.pack(side=LEFT, padx=5,ipadx=1,ipady=1)
        
    def Homepage(self):
        scroll_frame=customtkinter.CTkScrollableFrame(self,border_width=1,width=600,height=400,bg_color="white",fg_color="white")
        heading_font=customtkinter.CTkFont(family="Cooper Black",weight="bold",size=27)
        heading=Label(scroll_frame,text="Real Peanut Butter",font=heading_font,background="white")
        subheading=Label(scroll_frame,text="Made from premium peanuts. Slow roasted. Stone ground.",font="Arial 13",background="white")
        subheading2=Label(scroll_frame,text="No palm oil. No preservatives",font="Arial 13",background="white")
        scroll_frame.pack(expand=True,fill=BOTH,padx=4,pady=4)
        heading.pack(pady=5)
        subheading.pack(pady=4)
        subheading2.pack(pady=1)
        Learnmore=customtkinter.CTkButton(scroll_frame,
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
        Buynow=customtkinter.CTkButton(scroll_frame,
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
    
