import tkinter as tk
import tkinter.messagebox as tmsg
import customtkinter
from PIL import ImageTk, Image

self = customtkinter.CTk()
self.title("Brewphoria Cafe")
self.geometry("600x400")
self.minsize(600, 400)

def _show_products():
    tmsg.showinfo("Products", "Product list would appear here.")

bg_img_path = "C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\Coffee image backround.jpg"

# Canvas first
canvas = tk.Canvas(self, bd=0, highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Load and draw image
img = Image.open(bg_img_path)
background = ImageTk.PhotoImage(img)
canvas_img = canvas.create_image(0, 0, image=background, anchor="nw")

# Resize image with window
def resize_bg(event):
    resized = img.resize((event.width, event.height), Image.LANCZOS)
    canvas.bg_photo = ImageTk.PhotoImage(resized)
    canvas.itemconfig(canvas_img, image=canvas.bg_photo)

self.bind("<Configure>", resize_bg)

# --- Widgets on canvas using create_window ---

title_label = tk.Label(
    canvas,
    text="Welcome to Brewphoria Cafe!",
    font=("Bell MT", 20, "bold"),
    bg="#6b3a2a",
    fg="white"
)
canvas.create_window(300, 80, window=title_label)

description = (
    "At Brewphoria, every cup tells a story.\n"
    "We craft more than just coffee — we create moments of pure bliss,\n"
    "one perfectly brewed sip at a time. Whether you're chasing your morning spark\n"
    "or savoring a quiet afternoon, our cozy corners and handcrafted brews\n"
    "are your escape from the everyday. Come for the coffee, stay for the feeling."
)
desc_label = tk.Label(
    canvas,
    text=description,
    font=("Arial", 10),
    fg="white",
    bg="#6b3a2a",
    justify="center"
)
canvas.create_window(300, 220, window=desc_label)

customtkinter.set_appearance_mode("System")
button_font = customtkinter.CTkFont(family="Helvetica", size=14, weight="normal", slant="italic")

get_started = customtkinter.CTkButton(
    master=canvas,
    text="See Products >",
    font=button_font,
    text_color="black",
    command=_show_products,
    corner_radius=20,
    border_width=2,
    border_color="black",
    fg_color="#FFFFFF",
    hover_color="#6b3a2a"
)
canvas.create_window(300, 340, window=get_started)

self.mainloop() 