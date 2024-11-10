import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tabulation import tabulate_function

def plot():
    x_min = float(ent_x_min.get())
    x_max = float(ent_x_max.get())
    
    x, y = tabulate_function(x_min, x_max)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="f(x) = x^2 + sin(x)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=f)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

# Головне вікно
win = tk.Tk()
win.geometry("300x220")
win.configure(background = "blue")

# Введення x мінімального
Lx_min = tk.Label(win, text = "x мінімальне:", background = "blue", foreground = "white")
Lx_min.grid(row = 0, column = 0, padx = 7, pady = 7)
ent_x_min = tk.Entry(win)
ent_x_min.grid(row = 0, column = 1, padx = 7, pady = 7)

# Введення x максимального
Lx_max = tk.Label(win, text = "x максимальне:", background = "blue", foreground = "white")
Lx_max.grid(row = 1, column = 0, padx = 7, pady = 7)
ent_x_max = tk.Entry(win)
ent_x_max.grid(row = 1, column = 1, padx = 7, pady = 7)

#Кнопка для графіку
b = tk.Button(win, text = "Побудувати графік", command = plot)
b.grid(row=2, column=0, padx=5, pady=10)

#Вікно для графіку
f = tk.Frame(win)
f.grid(row=3, column = 0, padx = 5, pady = 5)

win.mainloop()