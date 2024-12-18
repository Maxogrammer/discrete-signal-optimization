from json import load
from os import path as ospath, listdir


def prime_divisors(n: int) -> list:
	'''
	Находит все простые делители числа, учитывая кратные.
	'''

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

def get_nums_from_file(phone_number: int, action_type: str) -> list:
	'''
	Отбирает данные нужного типа деятельности из
	одного файла Cipher/Phone[i]chr.json.
	'''

	current_directory = ospath.dirname(__file__)
	file_path = ospath.join(current_directory, '..', 'Data', 'PreparedExp', f'Phone{phone_number}.json')

	with open(file_path, 'r') as file:
		data = load(file)

		numbers = []
		for i in range(len(data)):
			cycle = data[i]
			for j in range(1, len(cycle)):
				pair = cycle[j]
				numbers.append(pair[0]) if (pair[1] == action_type) else None
	
	return numbers

def calc_tau(numbers: list) -> int:
	'''
	ЦНОД (Центрированный НОД) — считает tau.
	'''

	# Подсчёт количества всех простых делителей по отдельности
	data = {}
	total = 0

	for num in numbers:
		factors = list(set(prime_divisors(num))) # Не учитываем кратные множители

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

	print([(i-round(i/tau))/i for i in numbers])
	print([round(i/tau) for i in numbers])

	return tau


def find_tau(phone_number: int, action_type: str) -> int:
	'''
	Берёт данные 1 телефона за все циклы из файла Phone[i]chr.json,
	по специальному алгоритму находит tau.
	'''

	# Сбор данных
	numbers = get_nums_from_file(phone_number, action_type)

	# Расчёт tau
	tau = calc_tau(numbers)

	return tau

def find_tau_common(action_type: str) -> int:
	'''
	Берёт данные всех телефонов за все циклы из файлов Phone[i]chr.json,
	по специальному алгоритму находит tau.
	'''

	# Считает количество файлов
	current_directory = ospath.dirname(__file__)
	DIR = str(ospath.join(current_directory, '..', 'Data', 'PreparedExp'))

	files_num = len([name for name in listdir(DIR) if ospath.isfile(ospath.join(DIR, name))])

	# Сбор данных
	numbers = []
	for i in range(1, files_num + 1):
		numbers += get_nums_from_file(i, action_type)

	# Расчёт tau
	tau = calc_tau(numbers)

	return tau

def calc_tauN(numbers: list) -> float:
	'''
	Метод итераций.
	'''

	print(numbers)
	sum_T = sum(numbers)

	tau_cur = 0.999 * sum_T / len(numbers)
	tau_prev = 0
	while abs(tau_cur-tau_prev) > 0.001:
		tau_prev = tau_cur
		rounded_sum_T = sum([round(i/tau_cur) for i in numbers])
		tau_cur = sum_T / (rounded_sum_T)

	print([(i-round(i/tau_cur))/i for i in numbers])
	print([round(i/tau_cur) for i in numbers])

	return tau_cur
