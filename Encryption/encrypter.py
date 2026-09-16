from json import load
from os import path as ospath

'''
Преобразует целый цикл в строку используя шифр.
Модуль кодирования циклов активности в символьные последовательности
на основе рассчитанных интервалов дискретизации tau (ЦНОД и ММСП).

actions — список деятельности в виде [[время, тип], [время, тип] ...]
cipher_path — путь к файлу шифра в виде строки; пример: "Encryption\Cipher\Phone1.json"
'''

def encrypter(nomer_tsikla):
	result = ""
	result2 = ""

	current_directory = ospath.dirname(__file__)
	data_path = ospath.join(current_directory, ".." , 'Data', 'PreparedExp', 'Phone1.json')
	with open(data_path, "r") as data_path:
		data = load(data_path)

	cipher_path = ospath.join(current_directory, 'tau_CGCF.json')
	with open(cipher_path, "r") as cipher:
		phone_characteristics_data = load(cipher)

	for i1 in range(len(data[nomer_tsikla])):
		if i1 == 0:
			pass
		else:
			action_type = data[nomer_tsikla][i1][1]
			for i2 in range(int(data[nomer_tsikla][i1][0] / phone_characteristics_data[action_type])):
				result = result + action_type

	cipher_path = ospath.join(current_directory, 'tau_MMSE.json')
	with open(cipher_path, "r") as cipher:
		phone_characteristics_data = load(cipher)

	for i1 in range(len(data[nomer_tsikla])):
		if i1 == 0:
			pass
		else:
			action_type = data[nomer_tsikla][i1][1]
			for i2 in range(int(data[nomer_tsikla][i1][0] / phone_characteristics_data[action_type])):
				result2 = result2 + action_type
	

	return result, result2
