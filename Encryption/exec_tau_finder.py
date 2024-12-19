from json import load, dump
from os import path as ospath

from ideal_interval import find_tau_common


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

input('Press any key to exit: ')
