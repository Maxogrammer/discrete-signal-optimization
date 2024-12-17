import tkinter as tk
from tkinter import filedialog, messagebox
import json
from json import dump, load
from os import path as ospath
import matplotlib.pyplot as plt
import re
import ast
import prepare1, encrypter1

window = tk.Tk()
window.title("График зависимости заряда батареи от времени")
window.geometry("800x600")
text_for_terminal = "___"
text_for_terminal1 = "___"
text_for_txt = "___"
terminal = tk.Text(window)
terminal.place_configure(x=10, y=40, width=700, height=200)
# terminal1 = tk.Label(window, text=text_for_terminal1)
# terminal1.place_configure(x=10, y=80)
writen1 = []


# def enter():
# input1 = txt.get("1.0", tk.END)
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
    line1 = terminal.get("1.0", tk.END)

    char_counts = {}
    percent_counts = {}

    for char in line1:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    diff = 100

    first = 0
    sec = 0
    third = 0
    fourth = 0

    arr = []
    sum_value = 0

    for key, value in char_counts.items():
        sum_value += value
        arr.append(sum_value)

    for value in arr:
        print(value)

    for char, count in char_counts.items():
        if char == '@':
            percent_counts[char] = count * 0.675
        elif char == "O":
            percent_counts[char] = count * 0.0674
        elif char == "1":
            percent_counts[char] = count * 0.0974
        elif char == "&":
            percent_counts[char] = count * 0.676

    for char, count in percent_counts.items():
        if char == '@':
            diff -= count
            first = diff

        elif char == "O":
            diff -= count
            sec = diff

        elif char == "1":
            diff -= count
            third = diff

        elif char == "&":
            diff -= count
            fourth = diff

    if line1 != "":
        x_values = arr[:4]  # Используем массив arr для значений x
        y_values = [first, sec, third, fourth]

        plt.figure(figsize=(8, 6))
        plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label="Graph")
        plt.xlabel("Time (calculated from char_counts)")
        plt.ylabel("Values (first, sec, third, fourth)")
        plt.title("Graph of Calculated Values vs Time")
        plt.legend()
        plt.grid(True)
        plt.show()
def format_input(data_str):
    formatted = data_str.replace('{', '[').replace('}', ']')
    formatted = re.sub(r'(\d+)\s+([A-Za-z&@])', r'\1, "\2"', formatted)
    formatted = re.sub(r'(\d+)\s+(\d+)', r'\1, \2', formatted)
    formatted = formatted.replace('] [', '], [')
    return formatted
def load_and_plot():
    """Загружает данные и строит график."""
    data = load_json_file()
    if data:
        plot_graph(data)
###########################
def encr():
    global writen1
    #encrypter1.encrypter()
    txt.delete('1.0', tk.END)
    text_for_txt = encrypter1.encrypter()
    txt.insert(tk.END, text_for_txt)
###########################
def load_txt_file():
    file_path = filedialog.askopenfilename(title="Выберите TXT файл")
    try:
        data = open(file_path, "r")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить файл: {e}")
        return None
def prep(data):
    prepare1.prepare(data)
def load_for_prepare():
    try:
        file_path = filedialog.askopenfilename(title="Выберите TXT файл")
        data1 = open(file_path, "r",  encoding="utf-8")
        prep(data1)
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
#load_button = tk.Button(window, text="Загрузить JSON файл", command=load_and_plot)
#load_button.place_configure(x=105, y=10)
prepare_button = tk.Button(window, text="prepare", command=load_for_prepare, relief=tk.FLAT, bg="lightgrey")
prepare_button.place_configure(x=350, y=10)
txt = tk.Text(window, name='input')
txt.place_configure(x=10, y=450, width=700, height=40)
graph_paint = tk.Button(window, text="graph", command=plot_graph, relief=tk.FLAT, bg="lightgrey")
graph_paint.place_configure(x=10, y=420)
#enter_button = tk.Button(window, text="enter", command=enter)
#enter_button.place_configure(x=70, y=120)
encrypter_button = tk.Button(window, text="encrypt", command=encr, relief=tk.FLAT, bg="lightgrey")
encrypter_button.place_configure(x=410, y=10)

window.mainloop()