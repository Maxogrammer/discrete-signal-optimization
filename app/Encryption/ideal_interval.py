from json import load, dump
from os import path as ospath


def find_tau(phone_number: int, action_type: str) -> None:
	'''
	Берёт данные 1 телефона за все циклы из файла Phone[i]chr.json,
	по специальному алгоритму находит tau и записывает его в файл
	Cipher/Phone[i].json.
	'''

	# Алгоритм — умный НОД (УНОД)

	# Путь к данным
	current_directory = ospath.dirname(__file__)
	file_path = ospath.join(current_directory, '..', 'Data', 'PreparedExp', f'Phone{phone_number}chr.json')

	# Отбор данных нужного типа деятельности
	with open(file_path, 'r') as file:
		data = load(file)

		numbers = []
		for i in range(len(data)):
			cycle = data[i]
			for j in range(1, len(cycle)):
				pair = cycle[j]
				numbers.append(pair[0]) if (pair[1] == action_type) else None

	# Нахождение всех простых делителей
	def prime_divisors(n):
		i = 2
		factors = []
		while i * i <= n:
			if n % i:
				i += 1
			else:
				n //= i
				factors.append(i)
		if n > 1:
			factors.append(n)

		return factors

	# Подсчёт количества всех простых делителей по отдельности
	n = len(numbers)

	data = {}
	total = 0

	for num in numbers:
		factors = prime_divisors(num)

		for j in factors:
			total += 1

			try:
				data[j] += 1
			except KeyError:
				data[j] = 1

	# Сумма: суммарное кол-во простого делителя * простой делитель
	sum_tmp = 0
	for key in list(data.keys()):
		sum_tmp += key*data[key]

	# Идеальный интервал — сумма / суммарное кол-во всех простых делителей. По сути, центр масс.
	tau = sum_tmp // total

	# Сохранение tau
	file_path = ospath.join(current_directory, '..', 'Encryption', 'Cipher', f'Phone{phone_number}.json')

	with open(file_path, "r") as cipher:
		data = load(cipher)

	data[action_type]["tau"] = tau

	with open(file_path, "w") as cipher:
		dump(data, cipher, indent=4)


def find_tau_common(): pass
find_tau(2, "@")