import tkinter as tk
import tkinter.messagebox as tmsg
import customtkinter
from PIL import ImageTk,Image

self=customtkinter.CTk()
self.title("Brewphoria Cafe")
self.geometry("600x400")
self.minsize(600, 400)

def _show_products() :
    """Placeholder for the products page or dialog."""
    # future expansion: open a new window or update existing widgets
    tmsg.showinfo("Products", "Product list would appear here.")

def resize_bg(event):
    resized = img.resize((event.width, event.height), Image.LANCZOS)
    canvas.bg_photo = ImageTk.PhotoImage(resized)
    canvas.itemconfig(backround, image=canvas.backround)

# frame = tk.Frame(self, borderwidth=5, relief=tk.SUNKEN) 
# frame.pack(fill=tk.BOTH,expand=True)

bg_img_path="C:\\Users\\LOQ\\OneDrive\\Desktop\\sahaj code\\C-program\\Coffee image backround.jpg"
img=Image.open(bg_img_path)
backround=ImageTk.PhotoImage(img)

# label = tk.Label(self, text="Welcome!", font=("Helvetica", 24), bg="white")
canvas=tk.Canvas(self,width=backround.width(),height=backround.height(),bd=0,highlightthickness=0)
canvas.pack(fill=tk.BOTH,expand=True)
# canvas.create_window(backround.width() // 2, 50, window=label)
canvas.create_image(0, 0, image=backround,anchor="nw")

tk.Label(
    canvas,
    text="Welcome to Brewphoria Cafe!",
    font=("Bell MT", 20, "bold"),
).pack(pady=5)

description = (
    "At Brewphoria,\n"
    "every cup tells a story.\n"
    "We craft more than just coffee — we create moments of pure bliss,\n"
    "one perfectly brewed sip at a time. Whether you're chasing your morning spark or savoring a quiet afternoon,\n"
    "our cozy corners and handcrafted brews are your escape from the everyday. Come for the coffee,\n"
    "stay for the feeling."
)
tk.Label(canvas, text=description, font=("Arial", 10), fg="grey").pack(pady=5)

customtkinter.set_appearance_mode("System")
button_font=customtkinter.CTkFont(family="Helvatica",size=14,weight="normal",slant="italic")

get_started= customtkinter.CTkButton(
    master=canvas,
    text="See Products >",
    font=button_font,
    text_color="black",
    command=_show_products,
    corner_radius=20,
    border_width=2,
    border_color="black",
    fg_color="#FFFFFF",
    hover_color="#aa6100" 
)
get_started.pack(pady=5, ipadx=4, ipady=4)

self.mainloop()