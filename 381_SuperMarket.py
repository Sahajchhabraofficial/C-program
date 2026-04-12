import customtkinter as ctk
from tkinter import *

class Market(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x410")
        self.title("Super Market")
        self.minsize(600,400)

    # Colour pallets
    Cinder="#050408"
    Amethyst="#B46AC3"
    Purple_Heart="#512DAF"
    VooDoo="#593C5D"
    Sirocco="#747C7C"
            
    def ComingSoon(self):
        flag='GREEN'
        for widget in self.winfo_children():
            if flag=='RED':
                widget.pack_forget()
                print(type(widget))
                break
            else:
                flag='RED'
        ComingsoonFrame=ctk.CTkFrame(master=self,
                              width=30,
                              height=24,
                              bg_color=self.Sirocco,
                              borderwidth=1).pack(expand=True,fill=BOTH)
        Label(master=ComingsoonFrame,
              text="Coming Soon...",
              font=("Seoge UI",17,"bold")).pack(pady=52)
    
    def Cart(self):
        CartFrame=ctk.CTkFrame(master=self,
                     width=137,
                     border_color="white",
                     border_width=1,
                     fg_color="black")
        CartFrame.pack(side=RIGHT,fill=Y)
        #All Functions
        def Order():
            pass
        def Cancel():
            pass
        def close_Cart():
            CartFrame.destroy()
        ctk.CTkLabel(master=CartFrame,
              text="Your Cart",
              fg_color="black",
              text_color="white",
              font=("Helvatica",25,"bold")).grid(padx=5,pady=7,row=1,column=1)
        ctk.CTkButton(master=CartFrame,
                      text="❌",
                      font=("Seoge UI Emoji",13),
                      width=12,
                      command=close_Cart).grid(row=1,column=2,padx=5,pady=7)
    def Homepage(self):
        # flag='GREEN'
        # for widget in self.winfo_children():
        #     if flag=='RED':
        #         widget.pack_forget()
        #         print(type(widget))
        #         break
        #     else:
        #         flag='RED'
        # Menu Bar
        Menu_Bar = ctk.CTkFrame(master=self,
                fg_color=self.Sirocco,
                height=35)
        Menu_Bar.pack(side=TOP,fill=X,pady=4)

        Emoji=ctk.CTkFont(family="Seoge UI Emoji",size=25)
        def BuyNow():
            pass
        
        # Produts Tab
        ctk.CTkButton(master=Menu_Bar,
                     text="Products",
                     fg_color=self.Amethyst,
                     hover_color=self.Purple_Heart,
                     command=self.Homepage).pack(side=LEFT,padx=(5,10))
        # Coming Soon
        ctk.CTkButton(master=Menu_Bar,
                     text="Coming Soon",
                     fg_color=self.Amethyst,
                     hover_color=self.Purple_Heart,
                     command=self.ComingSoon).pack(side=LEFT,padx=7)
        #Your Cart
        ctk.CTkButton(master=Menu_Bar,
                     text="🛒",
                     font=Emoji,
                     fg_color=self.Amethyst,
                     hover_color=self.Purple_Heart,
                     width=30,
                     command=self.Cart).pack(side=LEFT,padx=(232,0))
        
        # Products Page
        Products_Page = ctk.CTkScrollableFrame(master=self,
                     fg_color="black",
                     border_width=1,
                     border_color="white")
        Products_Page.pack(side=LEFT,anchor='nw',fill=BOTH,expand=True)
        for i in range(4):
            #products line 1
            Product_line_1 = ctk.CTkFrame(master=Products_Page,
                         fg_color=self.VooDoo,
                         height=140,
                         width=140)
            Product_line_1.grid(row=0,column=i,pady=3,padx=3)
            ctk.CTkLabel(master=Product_line_1,
                         text=f"Product {i+1}",
                         text_color="white").pack(pady=(20,5))
            ctk.CTkButton(master=Product_line_1,
                          fg_color=self.Purple_Heart,
                          border_color="white",
                          border_width=1,
                          text_color="white",
                          text="Buy Now").pack(pady=(5))
            #products line 2
            Product_line_2 = ctk.CTkFrame(master=Products_Page,
                         fg_color=self.VooDoo,
                         height=140,
                         width=140)
            Product_line_2.grid(row=2,column=i,pady=3,padx=3)
            ctk.CTkLabel(master=Product_line_2,
                         text=f"Product {i+1}",
                         text_color="white").pack(pady=(20,5))
            ctk.CTkButton(master=Product_line_2,
                          fg_color=self.Purple_Heart,
                          border_color="white",
                          border_width=1,
                          text_color="white",
                          text="Buy Now").pack(pady=(5))
            #Products Line 3
            Product_line_3 = ctk.CTkFrame(master=Products_Page,
                         fg_color=self.VooDoo,
                         height=140,
                         width=140)
            Product_line_3.grid(row=3,column=i,pady=3,padx=3)
            ctk.CTkLabel(master=Product_line_3,
                         text=f"Product {i+1}",
                         text_color="white").pack(pady=(20,5))
            ctk.CTkButton(master=Product_line_3,
                          fg_color=self.Purple_Heart,
                          border_color="white",
                          border_width=1,
                          text_color="white",
                          text="Buy Now").pack(pady=(5))
            #Products line 4
            Product_line_4 = ctk.CTkFrame(master=Products_Page,
                         fg_color=self.VooDoo,
                         height=140,
                         width=140)
            Product_line_4.grid(row=4,column=i,pady=3,padx=3)
            ctk.CTkLabel(master=Product_line_4,
                         text=f"Product {i+1}",
                         text_color="white").pack(pady=(20,5))
            ctk.CTkButton(master=Product_line_4,
                          fg_color=self.Purple_Heart,
                          border_color="white",
                          border_width=1,
                          text_color="white",
                          text="Buy Now").pack(pady=(5))

        """ ctk.CTkButton(master=Products_Page,
                      text="Buy Now",
                      fg_color="#1f6aa5",
                      text_color="white",
                      width=120).grid(row=1,column=0,columnspan=4,pady=15)"""

if __name__== "__main__":
    App=Market()
    App.Homepage()
    App.mainloop()  