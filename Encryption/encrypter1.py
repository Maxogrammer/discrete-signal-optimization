'''
 /\/\/\/\/\/\/\/\/\   От кого: Рома
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
'''
from json import load
from os import path as ospath
'''
Преобразует целый цикл в строку используя шифр.

actions — список деятельности в виде [[время, тип], [время, тип] ...]
cipher_path — путь к файлу шифра в виде строки; пример: "Encryption\Cipher\Phone1.json"
'''
def encrypter():
	result = ""
	#text_for_terminal1 = ""
	#input1 = ""
	# num_cyc = input("Vvedite nomer  tsiklov: ")
	current_directory = ospath.dirname(__file__)
	data_path = ospath.join(current_directory, ".." , 'Data', 'PreparedExp', f'Phone99chr.json')
	with open(data_path, "r") as data_path:
		data = load(data_path)

	#text_for_terminal1 = 'Enter the mode (S — single phone / C — common calculations)'
	#while input1 == "":
		#enter()
	#mode = input1
	mode = input('Enter the mode (S — single phone / C — common calculations): ')
	match mode:
		case "C":
			current_directory = ospath.dirname(__file__)
			cipher_path = ospath.join(current_directory, f'tau_common.json')
			with open(cipher_path, "r") as cipher:
				phone_characteristics_data = load(cipher)
			nomer_tsikla = int(input("vvedite nomer stroki (pervaya stroka pod nomerom 0): "))
			for i1 in range(len(data[nomer_tsikla])):
				if i1 == 0:
					pass
				else:
					action_type = data[nomer_tsikla][i1][1]
					for i2 in range(int(data[nomer_tsikla][i1][0] / phone_characteristics_data[action_type])):
						result = result + action_type
			return result