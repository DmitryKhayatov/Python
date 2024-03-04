import tkinter as tk

def on_button_click():
    label.config(text="Привет, " + entry.get())

# Создаем основное окно
window = tk.Tk()
window.title("Пример приложения")

# Создаем и размещаем элементы интерфейса
label = tk.Label(window, text="Введите ваше имя:")
label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

button = tk.Button(window, text="Привет!", command=on_button_click)
button.pack(pady=10)

# Запускаем главный цикл обработки событий
window.mainloop()
