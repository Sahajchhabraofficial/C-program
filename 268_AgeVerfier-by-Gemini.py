import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import base64

# ==========================================
# ASSET: Embedded 'Shield' Icon (Base64)
# This allows the image to work without an external file.
# ==========================================
icon_data = """
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
QjkD/wL08N/X11X3AgAAAABJRU5ErkJggg==
"""

class AgeVerifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Identity Secure | Age Verification")
        self.root.geometry("450x550")
        self.root.configure(bg="#2c3e50")
        
        # Load the embedded image
        self.load_assets()
        
        # UI Styles
        self.setup_styles()
        
        # Build the Interface
        self.create_widgets()

    def load_assets(self):
        """Decodes the Base64 string into a PhotoImage for Tkinter"""
        try:
            image_bytes = base64.b64decode(icon_data)
            self.icon_image = tk.PhotoImage(data=image_bytes)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.icon_image = None

    def setup_styles(self):
        """Configures fonts and colors for a modern look"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Frame Styles
        self.style.configure("Card.TFrame", background="#34495e", relief="flat")
        
        # Label Styles
        self.style.configure("Header.TLabel", background="#34495e", foreground="#ecf0f1", font=("Helvetica", 18, "bold"))
        self.style.configure("Sub.TLabel", background="#34495e", foreground="#bdc3c7", font=("Helvetica", 10))
        self.style.configure("Result.TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Helvetica", 12))
        
        # Button Hover Effects
        self.style.map("Action.TButton",
            background=[('active', '#2980b9'), ('!active', '#3498db')],
            foreground=[('active', 'white'), ('!active', 'white')])
        self.style.configure("Action.TButton", font=("Helvetica", 11, "bold"), borderwidth=0, padding=10)

    def create_widgets(self):
        # --- Main Container ---
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # --- Card (Central Box) ---
        card = ttk.Frame(main_frame, style="Card.TFrame", padding=20)
        card.pack(fill="x", pady=20)

        # --- Icon/Image ---
        if self.icon_image:
            img_label = tk.Label(card, image=self.icon_image, bg="#34495e")
            img_label.pack(pady=(0, 10))

        # --- Title ---
        title = ttk.Label(card, text="Age Verification", style="Header.TLabel")
        title.pack()
        subtitle = ttk.Label(card, text="Please enter your date of birth below", style="Sub.TLabel")
        subtitle.pack(pady=(0, 20))

        # --- Input Section ---
        input_frame = tk.Frame(card, bg="#34495e")
        input_frame.pack(fill="x", pady=10)

        # Day
        tk.Label(input_frame, text="Day", bg="#34495e", fg="white").grid(row=0, column=0, padx=5)
        self.day_var = tk.StringVar()
        self.day_cb = ttk.Combobox(input_frame, textvariable=self.day_var, width=5, state="readonly")
        self.day_cb['values'] = [str(i) for i in range(1, 32)]
        self.day_cb.grid(row=1, column=0, padx=5)

        # Month
        tk.Label(input_frame, text="Month", bg="#34495e", fg="white").grid(row=0, column=1, padx=5)
        self.month_var = tk.StringVar()
        self.month_cb = ttk.Combobox(input_frame, textvariable=self.month_var, width=10, state="readonly")
        self.month_cb['values'] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.month_cb.grid(row=1, column=1, padx=5)

        # Year
        tk.Label(input_frame, text="Year", bg="#34495e", fg="white").grid(row=0, column=2, padx=5)
        self.year_var = tk.StringVar()
        current_year = date.today().year
        self.year_cb = ttk.Combobox(input_frame, textvariable=self.year_var, width=8, state="readonly")
        self.year_cb['values'] = [str(i) for i in range(current_year, 1900, -1)]
        self.year_cb.grid(row=1, column=2, padx=5)
        
        # Center grid
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(1, weight=1)
        input_frame.grid_columnconfigure(2, weight=1)

        # --- Button ---
        verify_btn = ttk.Button(card, text="VERIFY AGE", style="Action.TButton", command=self.verify_age)
        verify_btn.pack(fill="x", pady=25)

        # --- Status Area ---
        self.status_frame = tk.Frame(self.root, bg="#2c3e50", height=50)
        self.status_frame.pack(fill="x", padx=20)
        self.status_label = tk.Label(self.status_frame, text="", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 14))
        self.status_label.pack()

    def verify_age(self):
        # 1. Get Inputs
        d = self.day_var.get()
        m_str = self.month_var.get()
        y = self.year_var.get()

        # 2. Validation
        if not d or not m_str or not y:
            messagebox.showwarning("Missing Info", "Please select Day, Month, and Year.")
            return

        month_map = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, 
                     "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        
        try:
            birth_date = date(int(y), month_map[m_str], int(d))
        except ValueError:
            messagebox.showerror("Invalid Date", "The date you entered does not exist (e.g., Feb 30).")
            return

        # 3. Calculation Logic
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # 4. Result & Visual Feedback
        if age >= 18:
            self.show_success(age)
        else:
            self.show_denial(age)

    def show_success(self, age):
        self.root.configure(bg="#27ae60") # Green background
        self.status_frame.configure(bg="#27ae60")
        self.status_label.configure(text=f"ACCESS GRANTED\nAge: {age}", bg="#27ae60", fg="white")
        messagebox.showinfo("Success", f"You are {age} years old. Access Granted!")

    def show_denial(self, age):
        self.root.configure(bg="#c0392b") # Red background
        self.status_frame.configure(bg="#c0392b")
        self.status_label.configure(text=f"ACCESS DENIED\nAge: {age}", bg="#c0392b", fg="white")
        messagebox.showerror("Restricted", f"You are {age} years old. You must be 18+.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeVerifierApp(root)
    root.mainloop()