import customtkinter
from tkinter import *

root=Tk()
root.geometry("600x400")
root.title("Customtkinter sliders")
sliderVar=IntVar(value=0)      #slider var
# label=Label(root,textvariable=sliderVar)
"""def slider_event_value(value):
    label.configure(text=f"Value: {int(value)}")"""
slider=customtkinter.CTkSlider(master=root,         # main slider
                        height=150,
                        corner_radius=4,
                        button_corner_radius=2,
                        border_width=2,
                        border_color="black",
                        bg_color="white",
                        fg_color="white",
                        progress_color="green",
                        button_color="green",
                        button_hover_color="#6FFB62",
                        button_length=6,
                        number_of_steps=100,
                        width=20,
                        orientation="vertical",
                        from_=0,to=100,
                        state="normal",
                        # command=slider_event_value,
                        variable=sliderVar
                        ).pack(pady=6)
# slider.set(25)
slider_Value_label=Label(root,textvariable=sliderVar,font="Arial 15 bold") # label
slider_Value_label.pack(pady=4)

root.mainloop()