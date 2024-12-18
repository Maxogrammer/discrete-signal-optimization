import tkinter as tk
from tkinter import filedialog, messagebox
import json
from sys import path as syspath

import matplotlib.pyplot as plt

syspath.append('./')
import Data.prepare1 as prepare1, Encryption.encrypter1 as encrypter1

window = tk.Tk()
window.title("График зависимости заряда батареи от времени")
window.geometry("800x600")

text_for_terminal = "___"
text_for_terminal1 = "VVV Введите номер строки VVV"
text_for_txt = "___"

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

    line1 = txt.get("1.0", "100.0")
    if line1 != "":
        fig, ax = plt.subplots()
        ax.plot([1, 1.5, 2], [2, 1.8, 1])
        fig.show()

def load_and_plot():
    """Загружает данные и строит график."""
    data = load_json_file()
    if data:
        plot_graph(data)

###########################

def encr():
    global writen1
    txt.delete('1.0', tk.END)
    text_for_txt = encrypter1.encrypter(int(true_terminator.get("1.0", tk.END)))
    # print(int(true_terminator.get("1.0")))
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
    text_for_terminal = load_json_file()
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