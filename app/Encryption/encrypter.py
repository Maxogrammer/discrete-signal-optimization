from json import load


def convert_1type(t: int, action_type: str, cipher_path: str) -> str:
	'''
	Преобразовывает временной интервал в строку по шифру.
	'''

	with open(cipher_path, 'r') as cipher:
		data = load(cipher)[action_type]

		result = action_type*(t // data['tau'])

	return result

def convert_cycle():
	'''
	Преобразует целый цикл из Phone[i]chr.json в строку используя шифр.
	'''

	pass
