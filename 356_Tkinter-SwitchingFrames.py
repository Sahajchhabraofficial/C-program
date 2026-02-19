import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Switching Frames Demo")
        self.geometry("400x300")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        self.frames = {}
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, page_class):
        self.frames[page_class].tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Start Page", font=("Verdana", 12)).pack(pady=10)
        tk.Button(self, text="Go to Page One", command=lambda: controller.show_frame(PageOne)).pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Page One", font=("Verdana", 12)).pack(pady=10)
        tk.Button(self, text="Go to Start Page", command=lambda: controller.show_frame(StartPage)).pack()

if __name__ == "__main__":
    app = App()
    app.mainloop()
