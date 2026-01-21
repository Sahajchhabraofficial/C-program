import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageEnhance

# Configuration
APP_TITLE = "Apex Automotive | Luxury & Performance"
BG_IMAGE_PATH = "Car Wallpaper.jpg"
FONT_HEADER = ("Helvetica", 28, "bold")
FONT_SUBHEADER = ("Helvetica", 16)
FONT_BODY = ("Helvetica", 11)
ACCENT_COLOR = "#e74c3c"  # A sporty red

class CarApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1000x700")
        self.root.state('zoomed')  # Open full screen

        # Data: A simulated database of cars
        self.cars = [
            {"model": "Spectre GT", "price": "$120,000", "hp": "650 HP", "desc": "The ultimate grand tourer."},
            {"model": "Nebula X", "price": "$85,000", "hp": "450 HP", "desc": "Electric precision meets luxury."},
            {"model": "Viper Strike", "price": "$145,000", "hp": "720 HP", "desc": "Raw track performance."},
            {"model": "Horizon SUV", "price": "$95,000", "hp": "500 HP", "desc": "Comfort for the whole family."},
        ]

        # 1. Setup Background
        self.setup_background()

        # 2. Main Container (for switching pages)
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)
        
        # Make main frame semi-transparent hack (using a canvas overlay instead)
        self.main_frame.destroy() # We will use a Canvas for the "Website" feel

        # 3. Create the "Browser" Canvas
        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Draw the background image on the canvas
        self.draw_background()

        # Bind resize event to adjust background
        self.root.bind("<Configure>", self.resize_bg)

        # Start at Home Page
        self.show_home_page()

    def setup_background(self):
        """Loads and prepares the background image."""
        try:
            self.raw_bg = Image.open(BG_IMAGE_PATH)
            # Darken the image slightly so text pops
            enhancer = ImageEnhance.Brightness(self.raw_bg)
            self.raw_bg = enhancer.enhance(0.4) 
        except Exception as e:
            print(f"Error: {e}")
            # Fallback if image missing
            self.raw_bg = Image.new('RGB', (1920, 1080), color='#1a1a1a')
            messagebox.showerror("Image Error", f"Could not find '{BG_IMAGE_PATH}'. Using dark mode.")

    def draw_background(self):
        """Draws the background on the canvas."""
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        bg_resized = self.raw_bg.resize((w, h), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_resized)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw", tags="bg")

    def resize_bg(self, event):
        """Resizes background dynamically."""
        # Note: In a real app, adding a delay here prevents lag
        self.draw_background()
        self.canvas.tag_lower("bg") # Keep bg at the bottom

    def clear_canvas(self):
        """Removes UI elements but keeps the background."""
        self.canvas.delete("ui") # Delete everything tagged 'ui'

    # ==========================
    # PAGES
    # ==========================

    def show_home_page(self):
        self.clear_canvas()
        
        # Navbar simulation
        self.draw_navbar()

        # Hero Text
        self.canvas.create_text(100, 200, text="DRIVE THE EXTRAORDINARY", 
                                font=("Helvetica", 40, "bold"), fill="white", anchor="nw", tags="ui")
        self.canvas.create_text(100, 260, text="Experience engineering perfection.", 
                                font=("Helvetica", 18), fill="#bdc3c7", anchor="nw", tags="ui")

        # CTA Button
        self.create_button(100, 320, "VIEW INVENTORY", self.show_catalogue_page)

    def show_catalogue_page(self):
        self.clear_canvas()
        self.draw_navbar()

        self.canvas.create_text(50, 100, text="CURRENT INVENTORY", 
                                font=FONT_HEADER, fill="white", anchor="nw", tags="ui")

        # Grid of Cards
        start_x, start_y = 50, 180
        gap_x = 350 # Width of card + gap

        for index, car in enumerate(self.cars):
            x_pos = start_x + (index * gap_x)
            # Check for overflow and wrap (simplified logic)
            if x_pos > 1200: 
                x_pos = start_x + ((index-3) * gap_x)
                start_y = 500
            
            self.draw_car_card(x_pos, start_y, car)

    def show_purchase_page(self, car):
        self.clear_canvas()
        self.draw_navbar()

        # Split screen layout
        # Left Side: Details
        self.canvas.create_text(100, 150, text=car['model'], font=("Helvetica", 40, "bold"), fill="white", anchor="nw", tags="ui")
        self.canvas.create_text(100, 220, text=f"Price: {car['price']}", font=("Helvetica", 20), fill=ACCENT_COLOR, anchor="nw", tags="ui")
        self.canvas.create_text(100, 260, text=f"Power: {car['hp']}", font=("Helvetica", 16), fill="white", anchor="nw", tags="ui")
        self.canvas.create_text(100, 300, text=car['desc'], font=("Helvetica", 14), fill="#bdc3c7", anchor="nw", tags="ui")

        # Form Section Background
        self.canvas.create_rectangle(600, 150, 1000, 550, fill="#2c3e50", outline="white", tags="ui")
        self.canvas.create_text(620, 170, text="Order Configuration", font=("Helvetica", 18, "bold"), fill="white", anchor="nw", tags="ui")

        # Since we are on a canvas, we need to embed standard widgets using create_window
        # Name Entry
        name_lbl = tk.Label(self.root, text="Full Name", bg="#2c3e50", fg="white", font=FONT_BODY)
        name_ent = tk.Entry(self.root, font=FONT_BODY)
        self.canvas.create_window(800, 220, window=name_lbl, tags="ui")
        self.canvas.create_window(800, 250, window=name_ent, width=300, tags="ui")

        # Color Selection
        color_lbl = tk.Label(self.root, text="Select Color", bg="#2c3e50", fg="white", font=FONT_BODY)
        color_cb = ttk.Combobox(self.root, values=["Midnight Black", "Arctic White", "Rally Red", "Deep Blue"])
        self.canvas.create_window(800, 300, window=color_lbl, tags="ui")
        self.canvas.create_window(800, 330, window=color_cb, width=280, tags="ui")

        # Confirm Button
        def confirm_order():
            if not name_ent.get() or not color_cb.get():
                messagebox.showwarning("Incomplete", "Please fill out all fields.")
                return
            messagebox.showinfo("Order Placed", f"Congratulations {name_ent.get()}!\nYou have purchased the {car['model']} in {color_cb.get()}.")
            self.show_home_page()

        btn = tk.Button(self.root, text="CONFIRM PURCHASE", bg=ACCENT_COLOR, fg="white", font=("Helvetica", 12, "bold"), command=confirm_order)
        self.canvas.create_window(800, 450, window=btn, width=200, height=50, tags="ui")

    # ==========================
    # UI HELPERS
    # ==========================

    def draw_navbar(self):
        """Draws the top navigation bar."""
        # Semi-transparent bar at top
        self.canvas.create_rectangle(0, 0, 2000, 80, fill="#111", outline="", stipple="gray75", tags="ui")
        
        # Logo
        self.canvas.create_text(50, 25, text="APEX AUTOMOTIVE", font=("Helvetica", 20, "bold"), fill="white", anchor="nw", tags="ui")
        
        # Nav Buttons (Text acting as buttons)
        self.create_text_btn(1200, 35, "HOME", self.show_home_page)
        self.create_text_btn(1300, 35, "CARS", self.show_catalogue_page)
        self.create_text_btn(1400, 35, "CONTACT", lambda: messagebox.showinfo("Contact", "Call us at 555-0199"))

    def draw_car_card(self, x, y, car):
        """Draws a 'product card' on the canvas."""
        w, h = 300, 200
        
        # Card Background
        self.canvas.create_rectangle(x, y, x+w, y+h, fill="#000000", outline="#333", tags="ui")
        
        # Car Name
        self.canvas.create_text(x+20, y+20, text=car['model'], font=("Helvetica", 16, "bold"), fill="white", anchor="nw", tags="ui")
        
        # Car Price
        self.canvas.create_text(x+20, y+50, text=car['price'], font=("Helvetica", 12), fill=ACCENT_COLOR, anchor="nw", tags="ui")
        
        # Specs
        self.canvas.create_text(x+20, y+80, text=f"• {car['hp']}", font=("Helvetica", 10), fill="#bdc3c7", anchor="nw", tags="ui")
        
        # Buy Button specific to this car
        # We use a lambda default argument (c=car) to capture the specific car data
        btn = tk.Button(self.root, text="CONFIGURE", bg="white", fg="black", command=lambda c=car: self.show_purchase_page(c))
        self.canvas.create_window(x+150, y+160, window=btn, width=260, tags="ui")

    def create_button(self, x, y, text, command):
        """Draws a custom graphical button on canvas."""
        # We create a rectangle and text, and bind click events to both
        btn_bg = self.canvas.create_rectangle(x, y, x+200, y+50, fill=ACCENT_COLOR, outline=ACCENT_COLOR, tags="ui")
        btn_txt = self.canvas.create_text(x+100, y+25, text=text, fill="white", font=("Helvetica", 12, "bold"), tags="ui")
        
        # Bind events
        self.canvas.tag_bind(btn_bg, "<Button-1>", lambda e: command())
        self.canvas.tag_bind(btn_txt, "<Button-1>", lambda e: command())
        
        # Hover effect
        def on_enter(e): self.canvas.itemconfig(btn_bg, fill="#c0392b")
        def on_leave(e): self.canvas.itemconfig(btn_bg, fill=ACCENT_COLOR)
        
        self.canvas.tag_bind(btn_bg, "<Enter>", on_enter)
        self.canvas.tag_bind(btn_bg, "<Leave>", on_leave)

    def create_text_btn(self, x, y, text, command):
        """Creates a clickable text link."""
        t = self.canvas.create_text(x, y, text=text, fill="white", font=("Helvetica", 10, "bold"), tags="ui")
        self.canvas.tag_bind(t, "<Button-1>", lambda e: command())
        self.canvas.tag_bind(t, "<Enter>", lambda e: self.canvas.itemconfig(t, fill=ACCENT_COLOR))
        self.canvas.tag_bind(t, "<Leave>", lambda e: self.canvas.itemconfig(t, fill="white"))

if __name__ == "__main__":
    root = tk.Tk()
    app = CarApp(root)
    root.mainloop()