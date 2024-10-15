from json import load


def convert_cycle(actions: list, cipher_path: str) -> str:
	'''
	Преобразует целый цикл в строку используя шифр.

	actions — список деятельности в виде [[время, тип], [время, тип] ...]
	cipher_path — путь к файлу шифра в виде строки; пример: "Encryption\Cipher\Phone1.json"
	'''

	result = ''
	with open(cipher_path, 'r') as cipher:
		data = load(cipher)

	for action in actions:
		(t, action_type) = action
		tau = data[action_type]['tau']

		result += action_type*(t // tau)

	return result
