from tkinter import *
import customtkinter
from PIL import Image, ImageTk


class Swaadly(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Swaadly-clone")
        self.geometry("600x400")

        # keep references to images so they are not garbage‑collected
        self._logo_image = None
        self._bg_image = None

        self._create_menu()   # build menubar first
        self.Homepage()       # then show the homepage

    # ---- Menubar callbacks ----
    def products(self, value=None):
        print("Products clicked", value)

    def aboutus(self):
        print("About us clicked")

    def FAQs(self):
        print("FAQ clicked")

    # ---- UI construction helpers ----
    def _create_menu(self):
        menubar_frame = customtkinter.CTkFrame(
            self, bg_color="white", fg_color="white", border_width=0
        )
        menubar_frame.pack(side=TOP, fill=X, padx=8, pady=5)

        options_menu_font = customtkinter.CTkFont(family="Segoe UI", size=15)

        swaadly_logo_path = r"C:\Users\LOQ\OneDrive\Pictures\Screenshots\Screenshot 2026-02-27 130930.png"
        img = Image.open(swaadly_logo_path)
        self._logo_image = ImageTk.PhotoImage(img)
        swaadly_logo_button = customtkinter.CTkButton(
            menubar_frame,
            image=self._logo_image,
            text="",
            fg_color="white",
            bg_color="white",
            hover_color="white",
            command=self.Homepage,
            height=1,
        )
        swaadly_logo_button.pack(pady=(2, 6), padx=2, side=LEFT)

        products = ["Chocolate crunchy", "Creamy Chocolate", "Classic Original"]
        text = StringVar(value="Our Products")
        products_btn = customtkinter.CTkOptionMenu(
            menubar_frame,
            values=products,
            command=self.products,
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
            button_hover_color="white",
        )
        products_btn.pack(side=LEFT, padx=5)

        aboutus_btn = customtkinter.CTkButton(
            menubar_frame,
            text="About us",
            font=options_menu_font,
            command=self.aboutus,
            width=100,
            hover_color="white",
            bg_color="white",
            fg_color="white",
            text_color="#C48B4D",
            height=35,
        )
        aboutus_btn.pack(side=LEFT, padx=5, ipadx=1, ipady=1)

        faq_btn = customtkinter.CTkButton(
            menubar_frame,
            text="FAQ's",
            font=options_menu_font,
            command=self.FAQs,
            width=100,
            hover_color="white",
            bg_color="white",
            fg_color="white",
            text_color="#C48B4D",
            height=35,
        )
        faq_btn.pack(side=LEFT, padx=5, ipadx=1, ipady=1)

    def Homepage(self):
        # Load and display background image using Canvas
        bg_img_path = r"C:\Users\LOQ\OneDrive\Desktop\sahaj code\C-program\swaadly backround.jpg"
        pil_img = Image.open(bg_img_path)
        self._bg_image = ImageTk.PhotoImage(pil_img)
        
        # Create Canvas with background image
        self._background_image = Canvas(
            self, 
            width=600, 
            height=400, 
            bg="white", 
            highlightthickness=0
        )
        self._background_image.pack(expand=True, fill=BOTH)
        self._background_image.create_image(0, 0, image=self._bg_image, anchor="nw")
        
        # Create content frame using regular tkinter Frame
        content_frame = Frame(self._background_image, bg="white")
        self._background_image.create_window(300, 150, window=content_frame, width=550, height=300)

        heading_font = customtkinter.CTkFont(family="Cooper Black", weight="bold", size=27)
        heading = Label(content_frame, text="Real Peanut Butter", font=heading_font, bg="white", fg="black")
        subheading = Label(
            content_frame,
            text="Made from premium peanuts. Slow roasted. Stone ground.",
            font="Arial 13",
            bg="white",
            fg="black"
        )
        subheading2 = Label(content_frame, text="No palm oil. No preservatives", font="Arial 13", bg="white", fg="black")
        heading.pack(pady=5)
        subheading.pack(pady=4)
        subheading2.pack(pady=1)
        
        self._background_image.create_text( 100, 200,text="Real Peanut Butter",font=("Cooper Black", 16,"bold"))
      
        buttons_frame = Frame(content_frame, bg="white")
        buttons_frame.pack(pady=10)
        
        Learnmore = customtkinter.CTkButton(
            buttons_frame,
            text="Learn More >",
            corner_radius=50,
            width=100,
            hover_color="#CDCDCD",
            border_color="#000000",
            text_color="black",
            bg_color="white",
            fg_color="#ffffff",
            border_width=1,
        )
        Learnmore.pack(side=LEFT, padx=5)
        
        Buynow = customtkinter.CTkButton(
            buttons_frame,
            text="   Buy Now   ",
            corner_radius=50,
            width=100,
            hover_color="#2A7D35",
            border_color="#000000",
            text_color="black",
            bg_color="white",
            fg_color="#00B218",
            border_width=1,
        )
        Buynow.pack(side=LEFT, padx=5)


if __name__ == "__main__":
    app = Swaadly()
    app.mainloop()