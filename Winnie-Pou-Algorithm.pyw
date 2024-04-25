import customtkinter as tk
from tkinter import *
from matplotlib import pyplot as plt, patches
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
from PIL import Image
import math
import sys
import numpy as np

renders = 0

def close_properly():
    sys.exit()

def autosave():
    if autosave:
        global renders
        renders = renders + 1
        image_array = np.array(fig.canvas.renderer.buffer_rgba())
        image = Image.fromarray(image_array)
        image_rgb = image.convert("RGB")
        temp_path = "C:\\Users\\l13yo\\Documents\\Unterlagen Hofwil\\Privates\\Maou\\Coding with Kinu\\Winnie-Pou-Algorithm-main\\winnie_outputs\\winnie_"+str(renders)+".png"
        image_rgb.save(temp_path, format='png')

window = tk.CTk()

window.title("Winnie Pou Algorithm V1.1")
window.resizable(False, False)
window.protocol('WM_DELETE_WINDOW', close_properly)
font = tk.CTkFont(weight="bold")

plt.rcParams["figure.figsize"] = [7.00, 7.00]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.dpi"] = 100
fig = plt.figure()
fig.canvas.manager.set_window_title("Winnie Pou Algorithm")
fig.set_facecolor(color="#242424")
ax = fig.add_subplot()
ax.axes.format_coord = lambda x,y: ""
ax.set_facecolor(color="#242424")
ax.axes.set_facecolor(color="#242424")
ax.spines['bottom'].set_color('#dddddd')
ax.spines['top'].set_color('#dddddd') 
ax.spines['right'].set_color('#dddddd')
ax.spines['left'].set_color('#dddddd')
ax.tick_params(axis='both', colors='#dddddd')
for tick in ax.get_xticklabels():
    tick.set_fontname("Comic Sans MS")
    tick.set_fontweight("bold")
for tick in ax.get_yticklabels():
    tick.set_fontname("Comic Sans MS")
    tick.set_fontweight("bold")

class CustomToolbar(NavigationToolbar2Tk):
    def __init__(self, canvas, window=None, pack_toolbar=False):
        self.toolitems =  (
            ("Home", "Sweet Home :)", "home", "home"),
            ('Pan', 'Move', 'move', 'pan'),
            ('Zoom', 'Zoom', 'zoom_to_rect', 'zoom'),
            (None, None, None, None),
            ("Settings", "Settings to customize the Algorithm", "subplots", "settings_window_def"),
            (None, None, None, None)
        )
        self.flipflop = False
        super().__init__(canvas, window, pack_toolbar=pack_toolbar)

    def settings_window_def(self):
        def text_value_flipflop():
            global text_val
            if text_val:
                text_val = False
            else:
                text_val = True
            self.text_val_btn.configure(text=f'{text_val}')

        def autosave_value_flipflop():
            global autosave_val
            if autosave_val:
                autosave_val = False
            else:
                autosave_val = True
            self.autosave_val_btn.configure(text=f'{autosave_val}')

        def register():
            global current_placeholder_color_text
            global current_placeholder_color_circle
            if int(len(self.color_val_entry.get())) == 7:
                if self.color_val_entry.get()[0] == "#":
                    current_placeholder_color_text = self.color_val_entry.get()
                    current_placeholder_color_circle = self.color_val_entry.get()
                    self.autosave_val_btn.configure(fg_color=current_placeholder_color_text)
                    self.text_val_btn.configure(fg_color=current_placeholder_color_text)
                    render_btn.configure(fg_color=current_placeholder_color_text) #renderbutton
                    ax.spines['bottom'].set_color(current_placeholder_color_text) #ränder des Koordinatensystems:
                    ax.spines['top'].set_color(current_placeholder_color_text) 
                    ax.spines['right'].set_color(current_placeholder_color_text)
                    ax.spines['left'].set_color(current_placeholder_color_text)
                    ax.tick_params(axis='both', colors=current_placeholder_color_text)
                    canvas.draw()
                    

        def create_settings_window():
            global text_val
            global current_placeholder_color_text
            self.settings_window = tk.CTkToplevel(window)
            self.settings_window.geometry("500x250")
            self.settings_window.title("Settings")
            self.settings_window.resizable(False, False)
            self.settings_window.wm_transient(window)

            self.text_val_text = tk.CTkLabel(self.settings_window, text="Text Value:", font=font)
            self.autosave_val_text = tk.CTkLabel(self.settings_window, text="Autosave:", font=font)
            self.text_val_btn = tk.CTkButton(self.settings_window, text=f"{text_val}", fg_color=current_placeholder_color_text, font=font, command=text_value_flipflop)
            self.autosave_val_btn = tk.CTkButton(self.settings_window, text=f"{autosave_val}", fg_color=current_placeholder_color_text, font=font, command=autosave_value_flipflop)
            self.color_val_text = tk.CTkLabel(self.settings_window, text="Color Value:", font=font)
            self.color_val_entry = tk.CTkEntry(self.settings_window, placeholder_text=f"{current_placeholder_color_text}",font=font)
            self.color_val_btn = tk.CTkButton(self.settings_window, text="Register", fg_color="#50C878", hover_color="#2c6e42", font=font, command=register)

            self.text_val_text.grid(column=0, row=0, padx=(20, 5), pady=(15, 0))
            self.text_val_btn.grid(column=1, row=0, pady=(15, 0))
            self.autosave_val_text.grid(column=0, row=1, padx=(20, 5), pady=(3, 0))
            self.autosave_val_btn.grid(column=1, row=1, padx=(0, 0), pady=(5,0))
            self.color_val_text.grid(column=0, row=2, padx=(20, 5), pady=(3, 0))
            self.color_val_entry.grid(column=1, row=2, pady=(5, 0))
            self.color_val_btn.grid(column=2, row=2, padx=(5, 0), pady=(5, 0))

        if self.flipflop == True:
            if self.settings_window.winfo_exists() == False:
                create_settings_window()
        else:
            self.flipflop = True
            create_settings_window()


text_val = True
autosave_val = True
current_placeholder_color_text = "#1f6aa5"
current_placeholder_color_circle = "#dddddd"

canvas = FigureCanvasTkAgg(fig, master=window)
toolbar = CustomToolbar(canvas, window)
for i in range(-2, 6):
    toolbar.winfo_children()[i].config(background="#242424")
toolbar.config(background="#242424")

def send():
    try:
        ax.clear()
        radius_big_circle = float(big_circle.get())
        radius_small_circle = float(small_circle.get())
        all_circles = 0
        if radius_small_circle == radius_big_circle:
            text = ax.text(x=0, y=0, s="GAME OVER!", color=current_placeholder_color_circle, horizontalalignment="center", verticalalignment="center", size=50, clip_on=True)
        elif radius_small_circle > (radius_big_circle/2) and radius_small_circle < radius_big_circle:
            circle_calc = patches.Circle((0,0), fill=False, color=current_placeholder_color_circle, radius=radius_small_circle)
            if text_val:
                text = ax.text(x=0, y=0, s=1, color=current_placeholder_color_circle, horizontalalignment="center", verticalalignment="center", clip_on=True)
            ax.add_patch(circle_calc)
            all_circles = 1
        else:
            ib_1 = radius_big_circle - 2*radius_small_circle
            ib_storage = [ib_1]

            circle_storage = []

            circle_vals = []

            ib_val = ib_storage[0]

            while ib_val >= (2*radius_small_circle):
                ib_storage.append(ib_val - 2*radius_small_circle)
                ib_val = ib_val - 2*radius_small_circle

            for i in range(len(ib_storage)):
                a = 2*radius_small_circle
                b = ib_storage[i] + radius_small_circle
                c = ib_storage[i] + radius_small_circle

                alpha = ((math.acos((a**2-b**2-c**2)/(-2 * b * c)))*180)/math.pi

                circles = math.floor((360/(alpha-0.00000000000001)))

                corrected_value = 360 % (alpha-0.00000000000001)

                circle_vals.append(circles)

                for j in range(circles):
                    circle_calc = patches.Circle(((0 * math.cos(math.radians(j*(alpha+(corrected_value/circles)))) - (ib_storage[i]+radius_small_circle)*math.sin(math.radians(j*(alpha+(corrected_value/circles))))), ((0 * math.sin(math.radians(j*(alpha+(corrected_value/circles))))) + ((ib_storage[i]+radius_small_circle)*math.cos(math.radians(j*(alpha+(corrected_value/circles))))))), color=current_placeholder_color_circle, fill=False, radius=radius_small_circle)
                    if text_val:
                        text = ax.text(x=(0 * math.cos(math.radians(j*(alpha+(corrected_value/circles)))) - (ib_storage[i]+radius_small_circle)*math.sin(math.radians(j*(alpha+(corrected_value/circles))))),y=((0 * math.sin(math.radians(j*(alpha+(corrected_value/circles))))) + ((ib_storage[i]+radius_small_circle)*math.cos(math.radians(j*(alpha+(corrected_value/circles)))))),s=j+1, color=current_placeholder_color_circle, horizontalalignment="center", verticalalignment="center", clip_on=True)
                    circle_storage.append(circle_calc)

            for i in circle_storage:
                ax.add_patch(i)

            if ib_storage[len(ib_storage)-1] >= radius_small_circle:
                circle_extra = patches.Circle((0,0), radius=radius_small_circle, color=current_placeholder_color_circle, fill=False)
                all_circles = all_circles + 1
                if text_val:
                    text = ax.text(x=0,y=0, s=1, color=current_placeholder_color_circle, horizontalalignment="center", verticalalignment="center", clip_on=True)
                ax.add_patch(circle_extra)

            for i in circle_vals:
                all_circles = all_circles + i 

        circle1 = patches.Circle((0, 0), radius=radius_big_circle, color=current_placeholder_color_circle, fill=False)
        ax.add_patch(circle1)
        circle_val_text.configure(text=f'Circle Value: {all_circles}')
        space_used_calc = ((100/((radius_big_circle**2)*math.pi))*(((radius_small_circle**2)*math.pi)*all_circles))
        space_used_text.configure(text=f'Space Used: {space_used_calc} %')
        ax.axis("equal")

        canvas.draw()

        autosave()

        toolbar.update()
    except:
        pass

big_circle = tk.CTkEntry(master=window, width=150)
big_text = tk.CTkLabel(master=window, text="Big Circle Radius: ", font=font, width=16)
small_circle = tk.CTkEntry(master=window, width=150)
small_text = tk.CTkLabel(master=window, text="Small Circle Radius: ", font=font, width=16)
render_btn = tk.CTkButton(master=window, text="Render", font=font, width=150, command=send)
circle_val_text = tk.CTkLabel(master=window, text=f"Circle Value: VALUE", font=font, justify="left")
space_used_text = tk.CTkLabel(master=window, text=f"Space Used: VALUE%", font=font, justify="left")

big_text.grid(column=0, row=2, pady=5)
big_circle.grid(column=1, row=2)
small_text.grid(column=0, row=3, pady=5)
small_circle.grid(column=1, row=3)
render_btn.grid(column=1, row=4, pady=5)
circle_val_text.grid(column=2, row=2)
space_used_text.grid(column=2, row=3)
canvas.get_tk_widget().grid(column=0, row=0, columnspan=4)
toolbar.grid(column=0, row=1, pady=4)

window.mainloop()
