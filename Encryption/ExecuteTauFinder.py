from json import load, dump
from os import path as ospath

from ideal_interval import find_tau, find_tau_common


# Запрос режима работы
mode = input('Enter the mode (S — single phone / C — common calculations): ')
match mode:
	case 'C':
		# Чтение параметров
		action_type = input("Input the action type: ")
		
		# Получение tau
		tau = find_tau_common(action_type)

		# Сохранение tau
		current_directory = ospath.dirname(__file__)
		file_path = ospath.join(current_directory, '..', 'Encryption', f'tau_common.json')

		with open(file_path, "r") as cipher:
			data = load(cipher)

		data[action_type] = tau

		with open(file_path, "w") as cipher:
			dump(data, cipher, indent=4)

		print('Done!')
	case 'S':
		# Чтение параметров
		phone_number = input("Input the phone number: ")
		action_type = input("Input the action type: ")

		# Получение tau
		tau = find_tau(phone_number, action_type)

		# Сохранение tau
		current_directory = ospath.dirname(__file__)
		file_path = ospath.join(current_directory, '..', 'Encryption', 'Cipher', f'Phone{phone_number}.json')

		with open(file_path, "r") as cipher:
			data = load(cipher)

		data[action_type]["tau"] = tau

		with open(file_path, "w") as cipher:
			dump(data, cipher, indent=4)

		print('Done!')
	case _:
		print('Invalid input!')

input('Press any key to exit: ')
