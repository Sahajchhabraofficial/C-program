import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# ---------------------------------
# AutoDrive Pro - Showroom Edition
# ---------------------------------

class AutoDriveApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AutoDrive Pro | Virtual Showroom")
        self.geometry("1200x700")
        self.resizable(False, False)

        # Base Directory
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # Car Database
        self.cars = [
            {
                "name": "Ferrari SF90 Stradale",
                "price": "₹7.5 Crore",
                "type": "Hybrid Supercar",
                "file": "porshe02.jpg"
            },
            {
                "name": "Rolls-Royce Phantom VIII",
                "price": "₹9.5 Crore",
                "type": "Luxury Sedan",
                "file": "Rollsroyce01.jpg"
            },
            {
                "name": "Bugatti Chiron",
                "price": "₹28 Crore",
                "type": "Hypercar",
                "file": "Bugatti01.jpg"
            },
            {
                "name": "Mercedes-AMG GT R",
                "price": "₹3.2 Crore",
                "type": "Sports Coupe",
                "file": "Mercedes01.jpg"
            },
            {
                "name": "Tesla Roadster (2020)",
                "price": "₹2.8 Crore",
                "type": "Electric Supercar",
                "file": "Porshe01.jpg"
            },
            {
                "name": "Lamborghini Huracán EVO",
                "price": "₹4.1 Crore",
                "type": "Supercar",
                "file": "lambo01.jpg"
            }
        ]

        self.cart = []
        self.images = {}

        self.load_images()
        self.create_navbar()
        self.create_pages()

        self.show_page("home")

    # ---------------------------------
    # Image Loader
    # ---------------------------------
    def load_images(self):
        for car in self.cars:
            path = os.path.join(self.base_dir, car["file"])

            if not os.path.exists(path):
                messagebox.showerror("Missing File", f"{car['file']} not found")
                self.destroy()
                return

            img = Image.open(path)
            img = img.resize((260, 160))
            self.images[car["file"]] = ImageTk.PhotoImage(img)

    # ---------------------------------
    # Navigation Bar
    # ---------------------------------
    def create_navbar(self):
        self.navbar = tk.Frame(self, bg="#111")
        self.navbar.pack(fill="x")

        btn_style = {
            "font": ("Segoe UI", 12, "bold"),
            "bg": "#111",
            "fg": "white",
            "bd": 0,
            "activebackground": "#333"
        }

        tk.Button(self.navbar, text="Home", command=lambda: self.show_page("home"), **btn_style).pack(side="left", padx=20, pady=10)
        tk.Button(self.navbar, text="Showroom", command=lambda: self.show_page("gallery"), **btn_style).pack(side="left", padx=20)
        tk.Button(self.navbar, text="Cart", command=lambda: self.show_page("cart"), **btn_style).pack(side="left", padx=20)
        tk.Button(self.navbar, text="Support", command=lambda: self.show_page("support"), **btn_style).pack(side="left", padx=20)

    # ---------------------------------
    # Pages Setup
    # ---------------------------------
    def create_pages(self):
        self.pages = {}

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        for page in (HomePage, GalleryPage, CartPage, SupportPage):
            name = page.__name__.replace("Page", "").lower()
            frame = page(container, self)
            self.pages[name] = frame
            frame.place(relwidth=1, relheight=1)

    def show_page(self, name):
        self.pages[name].tkraise()


# =================================
# Home Page
# =================================
class HomePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#0f172a")

        tk.Label(
            self,
            text="Welcome to AutoDrive Pro",
            font=("Segoe UI", 36, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=40)

        tk.Label(
            self,
            text="India's Premium Virtual Car Showroom",
            font=("Segoe UI", 16),
            fg="#cbd5f5",
            bg="#0f172a"
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Explore Showroom",
            command=lambda: app.show_page("gallery")
        ).pack(pady=30, ipadx=20, ipady=8)


# =================================
# Gallery Page
# =================================
class GalleryPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#f8fafc")

        tk.Label(
            self,
            text="Car Showroom",
            font=("Segoe UI", 28, "bold"),
            bg="#f8fafc"
        ).pack(pady=20)

        grid = tk.Frame(self, bg="#f8fafc")
        grid.pack()

        row = 0
        col = 0

        for car in app.cars:
            card = tk.Frame(grid, bg="white", bd=1, relief="solid")
            card.grid(row=row, column=col, padx=20, pady=20)

            tk.Label(card, image=app.images[car["file"]], bg="white").pack(pady=5)

            tk.Label(card, text=car["name"], font=("Segoe UI", 11, "bold"), bg="white").pack()
            tk.Label(card, text=car["type"], bg="white").pack()
            tk.Label(card, text=car["price"], fg="green", bg="white").pack()

            ttk.Button(
                card,
                text="Add to Cart",
                command=lambda c=car: app.cart.append(c)
            ).pack(pady=5)

            col += 1
            if col == 3:
                col = 0
                row += 1


# =================================
# Cart Page
# =================================
class CartPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#f1f5f9")

        tk.Label(
            self,
            text="Your Cart",
            font=("Segoe UI", 26, "bold"),
            bg="#f1f5f9"
        ).pack(pady=20)

        self.listbox = tk.Listbox(self, font=("Segoe UI", 12), width=60, height=15)
        self.listbox.pack(pady=10)

        ttk.Button(
            self,
            text="Refresh Cart",
            command=lambda: self.load_cart(app)
        ).pack(pady=5)

        ttk.Button(
            self,
            text="Checkout",
            command=lambda: self.checkout(app)
        ).pack(pady=10)

    def load_cart(self, app):
        self.listbox.delete(0, "end")
        for car in app.cart:
            self.listbox.insert("end", f"{car['name']} - {car['price']}")

    def checkout(self, app):
        if not app.cart:
            messagebox.showwarning("Empty", "Your cart is empty")
            return

        messagebox.showinfo("Success", "Order placed successfully!")
        app.cart.clear()
        self.load_cart(app)


# =================================
# Support Page
# =================================
class SupportPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#020617")

        tk.Label(
            self,
            text="Customer Support",
            font=("Segoe UI", 28, "bold"),
            fg="white",
            bg="#020617"
        ).pack(pady=20)

        info = (
            "Email   : support@autodrive.com\n"
            "Phone   : +91 98765 43210\n"
            "Hours   : 24x7 Service\n\n"
            "Address : New Delhi, India"
        )

        tk.Label(
            self,
            text=info,
            font=("Segoe UI", 14),
            fg="#cbd5f5",
            bg="#020617",
            justify="left"
        ).pack(pady=20)


# =================================
# Run Application
# =================================
if __name__ == "__main__":
    app = AutoDriveApp()
    app.mainloop()