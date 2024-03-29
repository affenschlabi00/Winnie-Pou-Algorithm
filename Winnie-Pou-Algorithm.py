import tkinter as tk
from matplotlib import pyplot as plt, patches
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)
import math

window = tk.Tk()

window.geometry("700x820")
window.title("Winnie Pou Algorithm")

plt.rcParams["figure.figsize"] = [7.00, 7.00]
plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.dpi"] = 100
fig = plt.figure()
fig.canvas.manager.set_window_title("Winnie Pou Algorithm")
ax = fig.add_subplot()

canvas = FigureCanvasTkAgg(fig, master=window)
toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)

text_val = True

def send():
    try:
        float(big_circle.get()) - 0.1
        float(small_circle.get()) - 0.1
        ax.clear()
        radius_big_circle = float(big_circle.get())
        radius_small_circle = float(small_circle.get())
        if radius_small_circle > (radius_big_circle/2) and radius_small_circle < radius_big_circle:
            circle_calc = patches.Circle((0,0), fill=False, radius=radius_small_circle)
            if text_val:
                text = ax.text(x=0, y=0, s=1,color="black",horizontalalignment="center",verticalalignment="center")
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
                    circle_calc = patches.Circle(((0 * math.cos(math.radians(j*(alpha+(corrected_value/circles)))) - (ib_storage[i]+radius_small_circle)*math.sin(math.radians(j*(alpha+(corrected_value/circles))))), ((0 * math.sin(math.radians(j*(alpha+(corrected_value/circles))))) + ((ib_storage[i]+radius_small_circle)*math.cos(math.radians(j*(alpha+(corrected_value/circles))))))), fill=False, radius=radius_small_circle)
                    if text_val:
                        text = ax.text(x=(0 * math.cos(math.radians(j*(alpha+(corrected_value/circles)))) - (ib_storage[i]+radius_small_circle)*math.sin(math.radians(j*(alpha+(corrected_value/circles))))),y=((0 * math.sin(math.radians(j*(alpha+(corrected_value/circles))))) + ((ib_storage[i]+radius_small_circle)*math.cos(math.radians(j*(alpha+(corrected_value/circles)))))),s=j+1,color="black",horizontalalignment="center",verticalalignment="center")
                    circle_storage.append(circle_calc)

            for i in circle_storage:
                ax.add_patch(i)

            all_circles = 0

            if ib_storage[len(ib_storage)-1] >= radius_small_circle:
                circle_extra = patches.Circle((0,0), radius=radius_small_circle, fill=False)
                all_circles = all_circles + 1
                if text_val:
                    text = ax.text(x=0,y=0, s=1, color="black", horizontalalignment="center",verticalalignment="center")
                ax.add_patch(circle_extra)

            for i in circle_vals:
                all_circles = all_circles + i

        circle1 = patches.Circle((0, 0), radius=radius_big_circle, fill=False)
        ax.add_patch(circle1)

        settings_text.configure(text=f'Circle Value: {all_circles}')
        ax.axis("equal")

        canvas.draw()

        toolbar.update()
    except:
        pass

big_circle = tk.Entry(bg="grey", fg="white", width=16, bd=2)
big_text = tk.Label(text="Big Circle Radius: ", width=16)
small_circle = tk.Entry(bg="grey", fg="white", width=16, bd=2)
small_text = tk.Label(text="Small Circle Radius: ", width=16)
render_btn = tk.Button(text="Render",width=16, command=send)
settings_text = tk.Label(text=f"Circle Value: VALUE", width=16)

big_text.grid(column=0, row=2)
big_circle.grid(column=1, row=2)
small_text.grid(column=0, row=3)
small_circle.grid(column=1, row=3)
render_btn.grid(column=1, row=4)
settings_text.grid(column=2, row=2)
canvas.get_tk_widget().grid(column=0, row=0, columnspan=100)
toolbar.grid(column=0,row=1, columnspan=100, sticky="W")

window.mainloop()