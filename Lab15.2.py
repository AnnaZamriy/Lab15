import tkinter as tk

# Функція для зчитування масиву з файлу, сортування і виведення результату
def sort():
    masiv = list(map(int, entry.get().split()))

    masiv.sort(reverse=True)

    with open("masiv.txt", "w") as file:
        file.write(" ".join(map(str, masiv)))

# Головне вікно програми
win = tk.Tk()

f = tk.Frame(win, bg="blue")
f.pack(pady=10)

# Поле для введення масиву
l = tk.Label(f, text="Введіть масив:", bg="blue")
l.grid(row=1, column=0, padx=5, pady=5)

entry = tk.Entry(f, width=50)
entry.grid(row=1, column=1, padx=5, pady=5)

# Кнопка для запуску сортування
button = tk.Button(f, text="Сортувати", command=sort)
button.grid(row=2, column=0, pady=10)

win.mainloop()
