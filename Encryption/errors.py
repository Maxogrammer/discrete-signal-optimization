from sys import path as syspath
from os import path as ospath

import json

syspath.append('./')

current_directory = ospath.dirname(__file__)
data_path = ospath.join(current_directory, ".." , 'Data', 'PreparedExp', 'Phone1.json')

with open(data_path, "r") as file:
	full_data = json.load(file)

with open(ospath.join(current_directory, 'tau_CGCF.json'), "r") as file:
	tau_CGCF = json.load(file)

with open(ospath.join(current_directory, 'tau_MMSE.json'), "r") as file:
	tau_MMSE = json.load(file)


def calc(tau_cur):
	deltas = []
	epss = []
	int_deltas = []
	int_epss = []

	g_deltas = {'O': [],
			 	'I': [],
			 	'&': [],
			 	'@': []}
	
	m_err_deltas = {'O': [],
			 	'I': [],
			 	'&': [],
			 	'@': []}


	for i in range(len(full_data)):
		cycle = full_data[i][1:]	

		deltas_t = []
		epss_t = []

		T = 0
		for pair in cycle:
			time, symbol = pair

			# Delta
			round_t = round(time / tau_cur[symbol])
			delta = abs(time - round_t*tau_cur[symbol])
			deltas_t.append(delta)
			m_err_deltas[symbol].append(1+round_t/time)

			# Goodness
			g_deltas[symbol].append(delta)

			# Espilon
			eps = delta / time
			epss_t.append(eps)

			T += time

		# Integral values
		# Delta
		int_delta = sum(deltas_t)
		int_deltas.append(int_delta)

		# Epsilon
		int_eps = int_delta / T
		int_epss.append(int_eps)

		# Save
		deltas += deltas_t
		epss += epss_t


	min_eps, max_eps, aver_eps = min(epss), max(epss), sum(epss)/len(epss)
	min_delta, max_delta, aver_delta = min(deltas), max(deltas), sum(deltas)/len(deltas)

	min_int_delta, max_int_delta, aver_int_delta = min(int_deltas), max(int_deltas), sum(int_deltas)/len(int_deltas)
	min_int_eps, max_int_eps, aver_int_eps = min(int_epss), max(int_epss), sum(int_epss)/len(int_epss)

	print(min_delta, max_delta, aver_delta)
	print(100*min_eps, 100*max_eps, 100*aver_eps)
	print()

	print(min_int_delta, max_int_delta, aver_int_delta)
	print(100*min_int_eps, 100*max_int_eps, 100*aver_int_eps)
	print('\n')

	for i in g_deltas.keys():
		print(min(g_deltas[i])/tau_cur[i]*100, max(g_deltas[i])/tau_cur[i]*100, sum(g_deltas[i])/len(g_deltas[i])/tau_cur[i]*100)

	# print()
	# for i in g_deltas.keys():
	# 	print(min(g_deltas[i])/tau_cur[i]*100, max(g_deltas[i])/tau_cur[i]*100, sum(g_deltas[i])/len(g_deltas[i])/tau_cur[i]*100)

	# s = 0
	# n = 0
	# for i in g_deltas.keys():
	# 	s += sum(m_err_deltas[i])
	# 	n += len(m_err_deltas[i])
	# print(s/n)


calc(tau_CGCF)
print("-----------------------------------------------------------")
calc(tau_MMSE)
