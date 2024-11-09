'''
/\/\/\/\/\/\/\/\/\    От кого: Рома
/          --O--   \  Откуда: Минская область, г.Минск, ул.Октябрьская, дом 2
\    /\     /|\ ~~ /  Индекс: 220030
/   /^^\ /\    ~~~~\
\  /    /^^\  ~~~  /  Кому: Максим
/ /    /  ___ |    \  Куда: Минская область, г.Минск, ул.Октябрьская, дом 2
\--------/___\|----/  Индекс: 220030
/       /| # |\    \
\        |П  |     /
 \/\/\/\/\/\/\/\/\/
                     /\/\
                     \  /
 Код написан с любовь \/ на долгую память 05.11.2024

Преобразует целый цикл в строку используя шифр.

actions — список деятельности в виде [[время, тип], [время, тип] ...]
cipher_path — путь к файлу шифра в виде строки; пример: "Encryption\Cipher\Phone1.json"
'''
from json import load
from os import path as ospath
result = ""
# result - это наша готовая строка в будущем

#номер циклов - это Phnoe2chr.json например. Но вообщем циклы это время, прошедшее между моментом ,когда мы сняли телефон с зарядки,
# и моментом, когда мы его на зарядку поставили.
num_cyc = input("Enter the number of cycles: ")

#делаем data. data - это собственно информация из того .json.
current_directory = ospath.dirname(__file__)
data_path = ospath.join(current_directory, 'PreparedExp', f'Phone{num_cyc}chr.json')
with open(data_path, "r") as data_path:
	data = load(data_path)

#нам нужно дать пользователю возможность выбрать:
# использовать средние значения периода разрядки для разных видов действий или же для отдельного телефон
mode = input('Enter the mode (S — single phone / C — common calculations): ')
match mode:
    #C - common, то есть средние знаячения
	case "C":

        #открываем сами средние периоды
		cipher_path = ospath.join(current_directory, '..', 'Encryption', f'tau_common.json')
		with open(cipher_path, "r") as cipher:
			phone_characteristics_data = load(cipher)

        #спрашиваем у пользователя, какой номер строчки он хочет обработать
		nomer_tsikla = int(input("Enter the line number (first line numbered 0): "))

        #перебираем все виды действий в нашем списке того, чем разряжали телефон
		for i1 in range(1, len(data[nomer_tsikla])):
			action_type = data[nomer_tsikla][i1][1]

            #ну и на конец создаем саму строчку, деля время, затраченное на действие, на период самого действия.
			for i2 in range(int(data[nomer_tsikla][i1][0] / phone_characteristics_data[action_type])):
				result = result + action_type


    #S - для каждого отдельного телефона
	case "S":

        # открываем периоды телефона
		phone_number = input("Input the phone number: ")
		cipher_path = ospath.join(current_directory, '..', 'Encryption', 'Cipher', f'Phone{phone_number}.json')
		with open(cipher_path, "r") as cipher:
			phone_characteristics_data = load(cipher)

        #спрашиваем у пользователя, какой номер строчки он хочет обработать
		nomer_tsikla = int(input("Enter the line number (first line numbered 0): "))

        # перебираем все виды действий в нашем списке того, чем разряжали телефон
		for i1 in range(1, len(data[nomer_tsikla])):
			action_type = data[nomer_tsikla][i1][1]

            # ну и на конец создаем саму строчку, деля время, затраченное на действие, на период самого действия.
			for i2 in range(int(data[nomer_tsikla][i1][0] / phone_characteristics_data[action_type]["tau"])):
				result = result + action_type

#выводим результат в терминал
print(result)
input('Press any key to exit: ')

#записываем результат в файл в папку
string_path = ospath.join(current_directory, 'Strings', f'Phone{num_cyc}str.txt')
with open(string_path, "w") as string_path:
	string_path.write(result)
