import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO

class CarDealership:
    def __init__(self, root):
        self.root = root
        self.root.title("Elite Motors - Luxury Car Dealership")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a1a')
        
        self.cart = []
        self.cars = [
            {
                "name": "Tesla Model S",
                "price": 94990,
                "hp": "1020 HP",
                "speed": "200 mph",
                "image": "https://images.unsplash.com/photo-1617788138017-80ad40651399?w=400&q=80"
            },
            {
                "name": "Porsche 911 Turbo",
                "price": 174300,
                "hp": "640 HP",
                "speed": "205 mph",
                "image": "https://images.unsplash.com/photo-1614162692292-7ac56d7f36c0?w=400&q=80"
            },
            {
                "name": "Mercedes AMG GT",
                "price": 118600,
                "hp": "523 HP",
                "speed": "193 mph",
                "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=400&q=80"
            },
            {
                "name": "BMW M4 Competition",
                "price": 74700,
                "hp": "503 HP",
                "speed": "180 mph",
                "image": "https://images.unsplash.com/photo-1617531653332-bd46c24f2068?w=400&q=80"
            },
            {
                "name": "Lamborghini Huracán",
                "price": 248295,
                "hp": "631 HP",
                "speed": "202 mph",
                "image": "https://images.unsplash.com/photo-1544636331-e26879cd4d9b?w=400&q=80"
            },
            {
                "name": "Ferrari F8 Tributo",
                "price": 276550,
                "hp": "710 HP",
                "speed": "211 mph",
                "image": "https://images.unsplash.com/photo-1592198084033-aade902d1aae?w=400&q=80"
            }
        ]
        
        self.setup_ui()
        
    def load_image(self, url, size=(200, 150)):
        try:
            with urllib.request.urlopen(url) as u:
                raw_data = u.read()
            image = Image.open(BytesIO(raw_data))
            image = image.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except:
            # Create a placeholder if image loading fails
            img = Image.new('RGB', size, color='#333333')
            return ImageTk.PhotoImage(img)
    
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#000000', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🚗 ELITE MOTORS", 
            font=('Arial', 28, 'bold'),
            bg='#000000',
            fg='#ff0000'
        )
        title_label.pack(side='left', padx=30, pady=20)
        
        cart_btn = tk.Button(
            header_frame,
            text=f"🛒 Cart ({len(self.cart)})",
            font=('Arial', 12, 'bold'),
            bg='#ff0000',
            fg='white',
            command=self.show_cart,
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=10
        )
        cart_btn.pack(side='right', padx=30, pady=20)
        self.cart_btn = cart_btn
        
        # Main container with scrollbar
        main_container = tk.Frame(self.root, bg='#1a1a1a')
        main_container.pack(fill='both', expand=True)
        
        canvas = tk.Canvas(main_container, bg='#1a1a1a', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_container, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#1a1a1a')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Welcome section
        welcome_frame = tk.Frame(scrollable_frame, bg='#0d0d0d', height=200)
        welcome_frame.pack(fill='x', padx=20, pady=20)
        
        welcome_title = tk.Label(
            welcome_frame,
            text="DRIVE YOUR DREAM",
            font=('Arial', 36, 'bold'),
            bg='#0d0d0d',
            fg='white'
        )
        welcome_title.pack(pady=(30, 10))
        
        welcome_subtitle = tk.Label(
            welcome_frame,
            text="Experience luxury, performance, and innovation",
            font=('Arial', 16),
            bg='#0d0d0d',
            fg='#cccccc'
        )
        welcome_subtitle.pack(pady=(0, 30))
        
        # Collection title
        collection_label = tk.Label(
            scrollable_frame,
            text="PREMIUM COLLECTION",
            font=('Arial', 24, 'bold'),
            bg='#1a1a1a',
            fg='white'
        )
        collection_label.pack(pady=20)
        
        # Car grid
        cars_frame = tk.Frame(scrollable_frame, bg='#1a1a1a')
        cars_frame.pack(padx=20, pady=10)
        
        for idx, car in enumerate(self.cars):
            row = idx // 3
            col = idx % 3
            self.create_car_card(cars_frame, car, row, col)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg='#0d0d0d', height=60)
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="© 2026 Elite Motors - Your Premier Luxury Car Dealer | Phone: +1 (555) 123-4567",
            font=('Arial', 10),
            bg='#0d0d0d',
            fg='#666666'
        )
        footer_label.pack(pady=20)
    
    def create_car_card(self, parent, car, row, col):
        card_frame = tk.Frame(
            parent,
            bg='#2a2a2a',
            relief='flat',
            bd=2,
            highlightbackground='#404040',
            highlightthickness=2
        )
        card_frame.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        
        # Load and display image
        photo = self.load_image(car['image'])
        car['photo'] = photo  # Keep reference
        
        img_label = tk.Label(card_frame, image=photo, bg='#2a2a2a')
        img_label.pack(pady=10)
        
        # Car name
        name_label = tk.Label(
            card_frame,
            text=car['name'],
            font=('Arial', 16, 'bold'),
            bg='#2a2a2a',
            fg='white'
        )
        name_label.pack(pady=(5, 5))
        
        # Price
        price_label = tk.Label(
            card_frame,
            text=f"${car['price']:,}",
            font=('Arial', 20, 'bold'),
            bg='#2a2a2a',
            fg='#ff0000'
        )
        price_label.pack(pady=5)
        
        # Specs
        specs_label = tk.Label(
            card_frame,
            text=f"{car['hp']} • {car['speed']}",
            font=('Arial', 11),
            bg='#2a2a2a',
            fg='#999999'
        )
        specs_label.pack(pady=5)
        
        # Buttons frame
        btn_frame = tk.Frame(card_frame, bg='#2a2a2a')
        btn_frame.pack(pady=15, fill='x', padx=10)
        
        # Add to cart button
        add_btn = tk.Button(
            btn_frame,
            text="ADD TO CART",
            font=('Arial', 11, 'bold'),
            bg='#ff0000',
            fg='white',
            command=lambda c=car: self.add_to_cart(c),
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=8
        )
        add_btn.pack(side='left', expand=True, fill='x', padx=(0, 5))
        
        # Details button
        details_btn = tk.Button(
            btn_frame,
            text="DETAILS",
            font=('Arial', 11, 'bold'),
            bg='#404040',
            fg='white',
            command=lambda c=car: self.show_details(c),
            cursor='hand2',
            relief='flat',
            padx=20,
            pady=8
        )
        details_btn.pack(side='right', expand=True, fill='x', padx=(5, 0))
    
    def add_to_cart(self, car):
        self.cart.append(car)
        self.cart_btn.config(text=f"🛒 Cart ({len(self.cart)})")
        messagebox.showinfo("Added to Cart", f"{car['name']} has been added to your cart!")
    
    def show_details(self, car):
        details_window = tk.Toplevel(self.root)
        details_window.title(f"{car['name']} - Details")
        details_window.geometry("500x600")
        details_window.configure(bg='#2a2a2a')
        
        # Image
        photo = self.load_image(car['image'], size=(400, 250))
        car['detail_photo'] = photo
        
        img_label = tk.Label(details_window, image=photo, bg='#2a2a2a')
        img_label.pack(pady=20)
        
        # Name
        name_label = tk.Label(
            details_window,
            text=car['name'],
            font=('Arial', 24, 'bold'),
            bg='#2a2a2a',
            fg='white'
        )
        name_label.pack(pady=10)
        
        # Price
        price_label = tk.Label(
            details_window,
            text=f"${car['price']:,}",
            font=('Arial', 28, 'bold'),
            bg='#2a2a2a',
            fg='#ff0000'
        )
        price_label.pack(pady=10)
        
        # Specs frame
        specs_frame = tk.Frame(details_window, bg='#1a1a1a')
        specs_frame.pack(pady=20, padx=40, fill='x')
        
        tk.Label(
            specs_frame,
            text="Power",
            font=('Arial', 10),
            bg='#1a1a1a',
            fg='#999999'
        ).grid(row=0, column=0, padx=20, pady=5)
        
        tk.Label(
            specs_frame,
            text=car['hp'],
            font=('Arial', 14, 'bold'),
            bg='#1a1a1a',
            fg='white'
        ).grid(row=1, column=0, padx=20, pady=5)
        
        tk.Label(
            specs_frame,
            text="Top Speed",
            font=('Arial', 10),
            bg='#1a1a1a',
            fg='#999999'
        ).grid(row=0, column=1, padx=20, pady=5)
        
        tk.Label(
            specs_frame,
            text=car['speed'],
            font=('Arial', 14, 'bold'),
            bg='#1a1a1a',
            fg='white'
        ).grid(row=1, column=1, padx=20, pady=5)
        
        # Add to cart button
        add_btn = tk.Button(
            details_window,
            text="ADD TO CART",
            font=('Arial', 14, 'bold'),
            bg='#ff0000',
            fg='white',
            command=lambda: [self.add_to_cart(car), details_window.destroy()],
            cursor='hand2',
            relief='flat',
            padx=40,
            pady=15
        )
        add_btn.pack(pady=30)
    
    def show_cart(self):
        cart_window = tk.Toplevel(self.root)
        cart_window.title("Shopping Cart")
        cart_window.geometry("600x700")
        cart_window.configure(bg='#2a2a2a')
        
        # Header
        header_label = tk.Label(
            cart_window,
            text="YOUR CART",
            font=('Arial', 24, 'bold'),
            bg='#2a2a2a',
            fg='white'
        )
        header_label.pack(pady=20)
        
        if not self.cart:
            empty_label = tk.Label(
                cart_window,
                text="Your cart is empty",
                font=('Arial', 14),
                bg='#2a2a2a',
                fg='#999999'
            )
            empty_label.pack(pady=100)
        else:
            # Scrollable frame for cart items
            canvas = tk.Canvas(cart_window, bg='#2a2a2a', highlightthickness=0, height=400)
            scrollbar = ttk.Scrollbar(cart_window, orient='vertical', command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg='#2a2a2a')
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side='left', fill='both', expand=True, padx=20)
            scrollbar.pack(side='right', fill='y')
            
            # Cart items
            for idx, car in enumerate(self.cart):
                item_frame = tk.Frame(scrollable_frame, bg='#1a1a1a', relief='solid', bd=1)
                item_frame.pack(fill='x', pady=5, padx=10)
                
                tk.Label(
                    item_frame,
                    text=car['name'],
                    font=('Arial', 12, 'bold'),
                    bg='#1a1a1a',
                    fg='white'
                ).pack(side='left', padx=15, pady=10)
                
                tk.Button(
                    item_frame,
                    text="✖",
                    font=('Arial', 10, 'bold'),
                    bg='#ff0000',
                    fg='white',
                    command=lambda i=idx: self.remove_from_cart(i, cart_window),
                    cursor='hand2',
                    relief='flat',
                    width=3
                ).pack(side='right', padx=15, pady=10)
                
                tk.Label(
                    item_frame,
                    text=f"${car['price']:,}",
                    font=('Arial', 12, 'bold'),
                    bg='#1a1a1a',
                    fg='#ff0000'
                ).pack(side='right', padx=15, pady=10)
            
            # Total
            total = sum(car['price'] for car in self.cart)
            
            total_frame = tk.Frame(cart_window, bg='#1a1a1a')
            total_frame.pack(fill='x', padx=20, pady=20)
            
            tk.Label(
                total_frame,
                text="TOTAL:",
                font=('Arial', 18, 'bold'),
                bg='#1a1a1a',
                fg='white'
            ).pack(side='left', padx=20, pady=15)
            
            tk.Label(
                total_frame,
                text=f"${total:,}",
                font=('Arial', 20, 'bold'),
                bg='#1a1a1a',
                fg='#ff0000'
            ).pack(side='right', padx=20, pady=15)
            
            # Checkout button
            checkout_btn = tk.Button(
                cart_window,
                text="PROCEED TO CHECKOUT",
                font=('Arial', 14, 'bold'),
                bg='#ff0000',
                fg='white',
                command=self.checkout,
                cursor='hand2',
                relief='flat',
                padx=40,
                pady=15
            )
            checkout_btn.pack(pady=10)
    
    def remove_from_cart(self, index, window):
        if 0 <= index < len(self.cart):
            removed = self.cart.pop(index)
            self.cart_btn.config(text=f"🛒 Cart ({len(self.cart)})")
            window.destroy()
            self.show_cart()
            messagebox.showinfo("Removed", f"{removed['name']} removed from cart")
    
    def checkout(self):
        total = sum(car['price'] for car in self.cart)
        car_names = '\n'.join([f"• {car['name']}" for car in self.cart])
        
        result = messagebox.askyesno(
            "Checkout",
            f"Complete purchase?\n\n{car_names}\n\nTotal: ${total:,}"
        )
        
        if result:
            messagebox.showinfo(
                "Success!",
                "Thank you for your purchase!\n\nYour luxury vehicles will be delivered soon."
            )
            self.cart.clear()
            self.cart_btn.config(text=f"🛒 Cart ({len(self.cart)})")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarDealership(root)
    root.mainloop()