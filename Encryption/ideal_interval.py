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

def calc_tau_CGCF(numbers: list) -> float:
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
	tau = round(sum_tmp / total, 1)

	return tau

def find_tau_CGCF(action_type: str) -> float:
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
	tau = calc_tau_CGCF(numbers)

	return tau

def calc_tau_MMSE(numbers: list) -> float:
	'''
	Метод минимизации суммы погрешностей.
	'''

	min_tau = max(numbers)
	min_delta = sum(numbers)

	delta_tau = 0.01
 
	tau = 1 + delta_tau
	while tau <= min(numbers):
		delta = sum([(i-round(i/tau, 3)*tau) for i in numbers])

		if min_delta >= delta:
			min_delta = delta
			min_tau = tau

		tau += delta_tau	

	return round(min_tau, 1)

def find_tau_MMSE(action_type: str) -> float:
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
	tau = calc_tau_MMSE(numbers)

	return tau
