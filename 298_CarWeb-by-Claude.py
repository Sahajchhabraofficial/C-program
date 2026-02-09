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
                "name": "Rolls-Royce Phantom",
                "price": 174300,
                "hp": "640 HP",
                "speed": "205 mph",
                "image": "data:image/jpeg;base64,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"
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