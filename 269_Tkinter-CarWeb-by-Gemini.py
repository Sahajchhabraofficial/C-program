import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageEnhance
import os

# --- Configuration ---
APP_TITLE = "Apex Automotive | Luxury & Performance"
BG_IMAGE_NAME = "Car Wallpaper.jpg"
FONT_HEADER = ("Helvetica", 28, "bold")
FONT_SUBHEADER = ("Helvetica", 16)
FONT_BODY = ("Helvetica", 11)
ACCENT_COLOR = "#e74c3c"

class CarApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1000x700")
        self.root.state('zoomed')

        # This list tracks active widgets (buttons/entries) so we can destroy them properly later
        self.widgets_to_cleanup = []

        self.cars = [
            {"model": "Spectre GT", "price": "$120,000", "hp": "650 HP", "desc": "The ultimate grand tourer."},
            {"model": "Nebula X", "price": "$85,000", "hp": "450 HP", "desc": "Electric precision meets luxury."},
            {"model": "Viper Strike", "price": "$145,000", "hp": "720 HP", "desc": "Raw track performance."},
            {"model": "Horizon SUV", "price": "$95,000", "hp": "500 HP", "desc": "Comfort for the whole family."},
        ]

        # 1. Setup Background
        self.setup_background()

        # 2. Create Canvas
        self.canvas = tk.Canvas(self.root, highlightthickness=0, bg="black")
        self.canvas.pack(fill="both", expand=True)

        # 3. Draw Background & Bind Resize
        self.draw_background()
        self.root.bind("<Configure>", self.resize_bg)

        # 4. Start App
        self.show_home_page()

    def setup_background(self):
        """Loads the background image safely."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, BG_IMAGE_NAME)
        
        try:
            self.raw_bg = Image.open(image_path)
            enhancer = ImageEnhance.Brightness(self.raw_bg)
            self.raw_bg = enhancer.enhance(0.4) # Darken image
        except Exception as e:
            print(f"Error: {e}")
            self.raw_bg = Image.new('RGB', (1920, 1080), color='#1a1a1a')

    def draw_background(self):
        """Draws background on canvas."""
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        # Prevent crash on startup if width is 1
        if w < 10 or h < 10: return 

        bg_resized = self.raw_bg.resize((w, h), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_resized)
        
        # Draw image at very bottom (tag='bg')
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw", tags="bg")

    def resize_bg(self, event):
        """Refreshes background on resize."""
        self.draw_background()
        self.canvas.tag_lower("bg") # FORCE background to be at the bottom layer

    def clear_canvas(self):
        """Cleans up the screen for the next page."""
        # 1. Delete all drawings (text, rectangles)
        self.canvas.delete("ui")
        
        # 2. Destroy all active widgets (Entries, Buttons) to prevent ghosting
        for widget in self.widgets_to_cleanup:
            widget.destroy()
        self.widgets_to_cleanup.clear()

    # ==========================
    # PAGES
    # ==========================

    def show_home_page(self):
        self.clear_canvas()
        self.draw_navbar()

        # Hero Text
        self.canvas.create_text(100, 200, text="DRIVE THE EXTRAORDINARY", 
                                font=("Helvetica", 40, "bold"), fill="white", anchor="nw", tags="ui")
        self.canvas.create_text(100, 260, text="Experience engineering perfection.", 
                                font=("Helvetica", 18), fill="#bdc3c7", anchor="nw", tags="ui")

        # CTA Button
        self.create_custom_btn(100, 320, "VIEW INVENTORY", self.show_catalogue_page)

    def show_catalogue_page(self):
        self.clear_canvas()
        self.draw_navbar()

        self.canvas.create_text(50, 100, text="CURRENT INVENTORY", font=FONT_HEADER, fill="white", anchor="nw", tags="ui")

        start_x, start_y = 50, 180
        gap_x = 350

        for index, car in enumerate(self.cars):
            x_pos = start_x + (index * gap_x)
            # Wrap to next row if screen is too small
            if x_pos > 1200: 
                x_pos = start_x + ((index-3) * gap_x)
                start_y = 500
            
            self.draw_car_card(x_pos, start_y, car)

    def show_purchase_page(self, car):
        self.clear_canvas()
        self.draw_navbar()

        # --- Left Side: Car Details ---
        self.canvas.create_text(100, 150, text=car['model'], font=("Helvetica", 40, "bold"), fill="white", anchor="nw", tags="ui")
        self.canvas.create_text(100, 220, text=f"Price: {car['price']}", font=("Helvetica", 20), fill=ACCENT_COLOR, anchor="nw", tags="ui")
        self.canvas.create_text(100, 260, text=f"Power: {car['hp']}", font=("Helvetica", 16), fill="white", anchor="nw", tags="ui")
        self.canvas.create_text(100, 300, text=car['desc'], font=("Helvetica", 14), fill="#bdc3c7", anchor="nw", tags="ui")

        # --- Right Side: Order Form ---
        # 1. Form Background Box
        self.canvas.create_rectangle(600, 150, 1000, 550, fill="#2c3e50", outline="white", tags="ui")
        self.canvas.create_text(620, 170, text="Order Configuration", font=("Helvetica", 18, "bold"), fill="white", anchor="nw", tags="ui")

        # 2. Name Label & Input
        # (Using create_text for the label instead of a widget - it's more stable)
        self.canvas.create_text(620, 220, text="Full Name", font=FONT_BODY, fill="white", anchor="nw", tags="ui")
        
        name_ent = tk.Entry(self.root, font=FONT_BODY)
        self.canvas.create_window(800, 250, window=name_ent, width=350, tags="ui")
        self.widgets_to_cleanup.append(name_ent) # Add to cleanup list

        # 3. Color Label & Input
        self.canvas.create_text(620, 300, text="Select Color", font=FONT_BODY, fill="white", anchor="nw", tags="ui")
        
        color_cb = ttk.Combobox(self.root, values=["Midnight Black", "Arctic White", "Rally Red", "Deep Blue"], state="readonly")
        self.canvas.create_window(800, 330, window=color_cb, width=330, tags="ui")
        self.widgets_to_cleanup.append(color_cb) # Add to cleanup list

        # 4. Confirm Button Logic
        def confirm_order():
            if not name_ent.get() or not color_cb.get():
                messagebox.showwarning("Incomplete", "Please fill out all fields.")
                return
            messagebox.showinfo("Order Placed", f"Congratulations {name_ent.get()}!\nYou have purchased the {car['model']} in {color_cb.get()}.")
            self.show_home_page()

        # Create the confirm button
        btn = tk.Button(self.root, text="CONFIRM PURCHASE", bg=ACCENT_COLOR, fg="white", font=("Helvetica", 12, "bold"), command=confirm_order)
        self.canvas.create_window(800, 450, window=btn, width=200, height=50, tags="ui")
        self.widgets_to_cleanup.append(btn) # Add to cleanup list

    # ==========================
    # UI HELPERS
    # ==========================

    def draw_navbar(self):
        """Draws the top navigation bar."""
        # Top bar background
        self.canvas.create_rectangle(0, 0, 2000, 80, fill="#111", outline="", stipple="gray75", tags="ui")
        
        # Logo
        self.canvas.create_text(50, 25, text="APEX AUTOMOTIVE", font=("Helvetica", 20, "bold"), fill="white", anchor="nw", tags="ui")
        
        # Menu Links
        self.create_text_link(1200, 35, "HOME", self.show_home_page)
        self.create_text_link(1300, 35, "CARS", self.show_catalogue_page)
        self.create_text_link(1400, 35, "CONTACT", lambda: messagebox.showinfo("Contact", "Call us at 555-0199"))

    def draw_car_card(self, x, y, car):
        """Draws a 'product card'."""
        w, h = 300, 220
        
        # Card Background
        self.canvas.create_rectangle(x, y, x+w, y+h, fill="#000000", outline="#333", tags="ui")
        
        # Text Info
        self.canvas.create_text(x+20, y+20, text=car['model'], font=("Helvetica", 16, "bold"), fill="white", anchor="nw", tags="ui")
        self.canvas.create_text(x+20, y+50, text=car['price'], font=("Helvetica", 12), fill=ACCENT_COLOR, anchor="nw", tags="ui")
        self.canvas.create_text(x+20, y+80, text=f"• {car['hp']}", font=("Helvetica", 10), fill="#bdc3c7", anchor="nw", tags="ui")
        
        # Configure Button
        # NOTE: We use a widget button here because drawing custom shapes for many cards is slow
        btn = tk.Button(self.root, text="CONFIGURE", bg="white", fg="black", command=lambda c=car: self.show_purchase_page(c))
        self.canvas.create_window(x+150, y+170, window=btn, width=260, tags="ui")
        self.widgets_to_cleanup.append(btn)

    def create_custom_btn(self, x, y, text, command):
        """Draws a custom graphical button (Rectangle + Text)."""
        # We draw this directly on canvas, so no need to add to cleanup list (tags="ui" handles it)
        btn_bg = self.canvas.create_rectangle(x, y, x+200, y+50, fill=ACCENT_COLOR, outline=ACCENT_COLOR, tags="ui")
        btn_txt = self.canvas.create_text(x+100, y+25, text=text, fill="white", font=("Helvetica", 12, "bold"), tags="ui")
        
        # Click Events
        self.canvas.tag_bind(btn_bg, "<Button-1>", lambda e: command())
        self.canvas.tag_bind(btn_txt, "<Button-1>", lambda e: command())

    def create_text_link(self, x, y, text, command):
        """Creates a clickable text link."""
        t = self.canvas.create_text(x, y, text=text, fill="white", font=("Helvetica", 10, "bold"), tags="ui")
        self.canvas.tag_bind(t, "<Button-1>", lambda e: command())
        # Hover Effect
        self.canvas.tag_bind(t, "<Enter>", lambda e: self.canvas.itemconfig(t, fill=ACCENT_COLOR))
        self.canvas.tag_bind(t, "<Leave>", lambda e: self.canvas.itemconfig(t, fill="white"))

if __name__ == "__main__":
    root = tk.Tk()
    app = CarApp(root)
    root.mainloop()