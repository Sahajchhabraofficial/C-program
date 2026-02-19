import tkinter as tk

root = tk.Tk()
root.title("Simple Frame Switch")
root.geometry("400x300")

def show_page_one():
    for widget in root.winfo_children():  # Clear the window
        widget.destroy()

    tk.Label(root, text="Page One", font=("Verdana", 12)).pack(pady=10)
    tk.Button(root, text="Go to Page Two", command=show_page_two).pack()

def show_page_two():
    for widget in root.winfo_children():  # Clear the window
        widget.destroy()

    tk.Label(root, text="Page Two", font=("Verdana", 12)).pack(pady=10)
    tk.Button(root, text="Go back to Page One", command=show_page_one).pack()

show_page_one()  # Start with page one
root.mainloop()