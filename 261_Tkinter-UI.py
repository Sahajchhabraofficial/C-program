from tkinter import *

root = Tk()
root.title("Tours and Travels App")
root.geometry("455x544")
root.minsize(400,300)
# Title Frame (pack in root)
title_frame = Frame(root, borderwidth=5, bg="black")
title_frame.pack(side="top", fill="x")

Label(
    title_frame,
    text="Welcome to Sahaj Tours and Travels",
    font=("Comic Sans MS", 16, "bold"),
    fg="white",
    bg="black"
).pack(pady=10)

# Main Form Frame (pack in root)
form_frame = Frame(root, bg="grey", borderwidth=4, relief=RAISED)
form_frame.pack(pady=20)

# Labels
Label(form_frame, text="Your Name:", font=("Arial", 14, "bold"), bg="grey").grid(row=0, column=0, sticky="w", padx=10, pady=5)
Label(form_frame, text="Phone No:", font=("Arial", 14, "bold"), bg="grey").grid(row=1, column=0, sticky="w", padx=10, pady=5)
Label(form_frame, text="No. of People:", font=("Arial", 14, "bold"), bg="grey").grid(row=2, column=0, sticky="w", padx=10, pady=5)
Label(form_frame, text="Budget:", font=("Arial", 14, "bold"), bg="grey").grid(row=3, column=0, sticky="w", padx=10, pady=5)

# Entries
Entry(form_frame, width=25).grid(row=0, column=1, padx=10, pady=5)
Entry(form_frame, width=25).grid(row=1, column=1, padx=10, pady=5)
Entry(form_frame, width=25).grid(row=2, column=1, padx=10, pady=5)

# Budget Options
Checkbutton(form_frame, text="₹1000", bg="grey").grid(row=4, column=0, pady=5)
Checkbutton(form_frame, text="₹3500", bg="grey").grid(row=4, column=1, pady=5)
Checkbutton(form_frame, text="₹7000", bg="grey").grid(row=4, column=2, pady=5)

root.mainloop()