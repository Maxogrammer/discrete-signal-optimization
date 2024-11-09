'''
Преобразовывает опыт (Exp) в вид, удобный для использования (.json).
Изначально должен уметь преобразовывать собранные нами .txt в .json, а именно:
	а) создавать файлы, где каждая деятельность указана в хронологическом порядке — chr
	б) создавать файлы, где найдена сумма каждой деятельности в каждом цикле — int
'''
#это баааааааза
import json
name = str(input("Введите название файла: "))
file = open("C:/Users/Роман/Desktop/Phone-charge-prediction-main/Phone-charge-prediction-main/Data/PersonalExp/" + name + ".txt", "r", encoding="utf-8")
file1 = open("C:/Users/Роман/Desktop/Phone-charge-prediction-main/Phone-charge-prediction-main/Data/PreparedExp/" + name + "(prepared).json", "w")
pr_list_beg = []
pr_list_end = []
else_list = []
else_list_num = []
else_list_let = []
finish_list = []
pr = []
c_list = []
finish_finish_list =[]
new_file = ""
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
counter = 0

#создание начального и конечного процентов как списков
for str1 in file:
    pr = []
    pr_end = []
    pr_beg = []
    pr_list_beg = []
    pr_list_end = []
    for el in str1:
        if counter == 1:
            if el != " ":
                pr_list_end.append(el)
            else:
                counter += 1
        if counter == 0:
            if el in numbers:
                pr_list_beg.append(el)
            if el == " ":
                #наличие пробела означает окончание предыдущего числа
                counter += 1

        #создание списка со всем, кроме начального и конечного процентов
        if counter >= 2:
            if el == "о":
                else_list.append("O")
            elif el == "з":
                else_list.append("I")
            elif el == "м":
                else_list.append("@")
            elif el == "в":
                else_list.append("&")
            else:
                else_list.append(el)
    # объеденение списоков в строки, а зате превращение их в числа
    pr_beg = "".join(pr_list_beg)
    pr_end = "".join(pr_list_end)
    pr_beg = int(pr_beg)
    pr_end = int(pr_end)
    pr.append(pr_beg)
    pr.append(pr_end)
    finish_list.append(pr)

    # обнуление счетчиков для дальнейшего их использования.
    # Удаление первого символа в спике, в котором есть все, кроме начального и конечного процентов, потому что мешает.
    counter = 0
    len_counter = 0
    else_list.pop(0)

    # разбор списка, в котором нет начального и конечного процентов, на отдельные списки
    for el in else_list:
        if counter == 1:
            # объединение списков из цифр и списка из букв в один список
            else_list_num_joined = "".join(else_list_num)
            else_list_num_joined = int(else_list_num_joined)
            else_list_let_joined = "".join(else_list_let)
            c_list.append(else_list_num_joined)
            c_list.append(else_list_let_joined)
            # удаление предыдущих списков с буквами и цифрами, чтобы затем по-новой их использовать
            else_list_let = []
            else_list_num = []
            counter = 0
            # добавление объедененного списка из цифры и буквы в конечный список
            finish_list.append(c_list)
            c_list = []
        if counter == 0:
            # создание списков с цифрами и буквами
            if el in numbers:
                else_list_num.append(el)
            if el not in numbers and el != " " and el != "\n":
                else_list_let.append(el)
            if el == " ":
                # наличие пробела означает окончание предыдущего числа с буквой
                counter += 1
            if el == "\n":
                if else_list_num == []:
                    exit
                else:
                    # объединение списков из цифр и списка из букв в один список
                    else_list_num_joined = "".join(else_list_num)
                    else_list_num_joined = int(else_list_num_joined)
                    else_list_let_joined = "".join(else_list_let)
                    c_list.append(else_list_num_joined)
                    c_list.append(else_list_let_joined)
                    # удаление предыдущих списков с буквами и цифрами, чтобы затем по-новой их использовать
                    else_list_let = []
                    else_list_num = []
                    counter = 0
                    # добавление объедененного списка из цифры и буквы в конечный список
                    finish_list.append(c_list)
                    c_list = []

    # добавление конечного списка в json файл
    finish_finish_list.append(finish_list)
    finish_list = []
    else_list = []

#добавление конечного списка в json файл
json.dump(finish_finish_list, file1, indent=4)
file1.close()
file.close()

