from json import load, dump
from os import path as ospath
from sys import path as syspath

from Encryption.ideal_interval import find_tau_CGCF, find_tau_MMSE

action_types = ['O', 'I', '@', '&']

def calc_taus():
	for action_type in action_types:
		# ЦНОД
		# Получение tau
		tau_CGCF = find_tau_CGCF(action_type)
		tau_MMSE = find_tau_MMSE(action_type)

		# Сохранение tau_CGCF
		current_directory = ospath.dirname(__file__)
		file_path = ospath.join(current_directory, '..', 'Encryption', f'tau_CGCF.json')

		with open(file_path, "r") as cipher:
			data = load(cipher)

		data[action_type] = tau_CGCF

		with open(file_path, "w") as cipher:
			dump(data, cipher, indent=4)

		# Сохранение tau_MMSE
		current_directory = ospath.dirname(__file__)
		file_path = ospath.join(current_directory, '..', 'Encryption', f'tau_MMSE.json')

		with open(file_path, "r") as cipher:
			data = load(cipher)

		data[action_type] = tau_MMSE

		with open(file_path, "w") as cipher:
			dump(data, cipher, indent=4)