import tkinter as tk
from tkinter import filedialog, messagebox
import json
from sys import path as syspath
from os import path as ospath

import matplotlib.pyplot as plt

syspath.append('./')
import Data.prepare as prepare1, Encryption.encrypter as encrypter1

window = tk.Tk()
window.title("График зависимости заряда батареи от времени")
window.geometry("800x600")

text_for_terminal = "___"
text_for_terminal1 = "VVV Введите номер строки VVV"
text_for_txt = "___"

usage_power = {
    '@': 0.0675,
    '&': 0.0676,
    'O': 0.0674,
    'I': 0.0674,    
}

terminal = tk.Text(window)
terminal.place_configure(x=10, y=40, width=700, height=200)

aboba_terminator = tk.Label(window, text=text_for_terminal1)
aboba_terminator.place_configure(x=10, y=270)

writen1 = []

def load_json_file():
    """Функция для выбора и загрузки JSON файла."""
    file_path = filedialog.askopenfilename(
        title="Выберите JSON файл",
        filetypes=[("JSON файлы", "*.json"), ("Все файлы", "*.*")]
    )
    if not file_path:
        return None

    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")
        return None

def plot_graph():
    """Функция для построения графика на основе данных."""

    ciphered_string = txt.get("1.0", tk.END)

    current_directory = ospath.dirname(__file__)
    data_path = ospath.join(current_directory, ".." , 'Data', 'PreparedExp', 'Phone1.json')
    
    with open(data_path, "r") as file:
        full_data = json.load(file)[int(true_terminator.get("1.0", tk.END)) - 1]
        perc0, perc_end, data = full_data[0][0], full_data[0][1], full_data[1:]

    current_directory = ospath.dirname(__file__)
    data_path = ospath.join(current_directory, ".." , 'Encryption', 'tau_common.json')
    
    with open(data_path, "r") as file:
        tau_dict = json.load(file)

    y_axis = [perc0]
    x_axis = [0]

    for i in range(len(ciphered_string) - 1):
        char = ciphered_string[i]

        x_axis.append(x_axis[-1] + tau_dict[char])
        y_axis.append(y_axis[-1] - usage_power[char]*tau_dict[char])

    y_orig = [perc0]
    x_orig = [0]

    for i in range(len(data)):
        x_orig.append(x_orig[-1] + data[i][0])
        y_orig.append(y_orig[-1] - usage_power[char]*data[i][0])

    plt.figure(figsize=(10, 6))
    plt.plot(x_axis, y_axis, marker='o', linestyle='-', color='b', label="С шифровкой", linewidth=0.5, markersize=3)
    plt.plot(x_orig, y_orig, marker='|', linestyle='dashed', color='g', label="Оригинал", linewidth=0.5, markersize=10)
    plt.plot([0, x_orig[-1]], [perc0, perc_end], marker=7, color='r', label="Начальная и конечная точки", linewidth=0, markersize=10)

    plt.xlabel("Время в течение цикла (мин)")
    plt.ylabel("Процент заряда телефона")
    plt.title("Зависимость заряда телефона от времени")
    plt.legend()
    plt.grid(True)
    plt.show()

def load_and_plot():
    """Загружает данные и строит график."""
    data = load_json_file()
    if data:
        plot_graph(data)

###########################

def encr():
    global writen1
    txt.delete('1.0', tk.END)
    text_for_txt = encrypter1.encrypter(int(true_terminator.get("1.0", tk.END)) - 1)

    txt.insert(tk.END, text_for_txt)

###########################

def load_txt_file():
    file_path = filedialog.askopenfilename(title="Выберите TXT файл")
    try:
        data = open(file_path, "r")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")
        return None

def load_for_prepare():
    try:
        file_path = filedialog.askopenfilename(title="Выберите TXT файл")
        data1 = open(file_path, "r",  encoding="utf-8")
        prepare1.prepare(data1)
    except NameError:
        pass

############################

def print1():
    terminal.delete("1.0", tk.END)

    current_directory = ospath.dirname(__file__)
    data_path = ospath.join(current_directory, ".." , 'Data', 'PreparedExp', 'Phone1.json')
    
    with open(data_path, "r") as file:
        text_for_terminal = json.load(file)

    terminal.insert(tk.END, text_for_terminal)

def clear():
    terminal.delete("1.0", tk.END)

############################

clear_button = tk.Button(window, text="clear", command=clear, relief=tk.FLAT, bg="lightgrey")
clear_button.place_configure(x=250, y=10)

print_button = tk.Button(window, text="print", command=print1, relief=tk.FLAT, bg="lightgrey")
print_button.place_configure(x=300, y=10)

prepare_button = tk.Button(window, text="prepare", command=load_for_prepare, relief=tk.FLAT, bg="lightgrey")
prepare_button.place_configure(x=350, y=10)

txt = tk.Text(window, name='input')
txt.place_configure(x=10, y=450, width=700, height=40)

graph_paint = tk.Button(window, text="graph", command=plot_graph, relief=tk.FLAT, bg="lightgrey")
graph_paint.place_configure(x=10, y=420)

encrypter_button = tk.Button(window, text="encrypt", command=encr, relief=tk.FLAT, bg="lightgrey")
encrypter_button.place_configure(x=410, y=10)

true_terminator = tk.Text(window)
true_terminator.place_configure(x=10, y=300, width=100, height=30)

window.mainloop()