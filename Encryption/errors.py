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


deltas_CGCF = []
deltas_MMSE = []

epss_CGCF = []
epss_MMSE = []



int_deltas_CGCF = []
int_deltas_MMSE = []

int_epss_CGCF = []
int_epss_MMSE = []

for i in range(len(full_data)):
	cycle = full_data[i][1:]	

	deltas_CGCF_t = []
	deltas_MMSE_t = []

	epss_CGCF_t = []
	epss_MMSE_t = []

	T = 0
	for pair in cycle:
		time, symbol = pair

		# Delta
		delta_CGCF = abs(time - round(time / tau_CGCF[symbol])*tau_CGCF[symbol])
		delta_MMSE = abs(time - round(time / tau_MMSE[symbol])*tau_MMSE[symbol])

		deltas_CGCF_t.append(delta_CGCF)
		deltas_MMSE_t.append(delta_MMSE)

		# Espilon
		eps_CGCF = delta_CGCF / time
		eps_MMSE = delta_MMSE / time

		epss_CGCF_t.append(eps_CGCF)
		epss_MMSE_t.append(eps_MMSE)

		T += time

	# Integral values
	# Delta
	int_delta_CGCF = sum(deltas_CGCF_t)
	int_delta_MMSE = sum(deltas_MMSE_t)

	int_deltas_CGCF.append(int_delta_CGCF)
	int_deltas_MMSE.append(int_delta_MMSE)

	# Epsilon
	int_eps_CGCF = int_delta_CGCF / T
	int_eps_MMSE = int_delta_MMSE / T

	int_epss_CGCF.append(int_eps_CGCF)
	int_epss_MMSE.append(int_eps_MMSE)	

	# Save
	deltas_CGCF += deltas_CGCF_t
	deltas_MMSE += deltas_MMSE_t

	epss_CGCF += epss_CGCF_t
	epss_MMSE += epss_MMSE_t


max_eps_CGCF, aver_eps_CGCF = max(epss_CGCF), sum(epss_CGCF)/len(epss_CGCF)
max_eps_MMSE, aver_eps_MMSE = max(epss_MMSE), sum(epss_MMSE)/len(epss_MMSE)

min_delta_CGCF, max_delta_CGCF, aver_delta_CGCF = min(deltas_CGCF), max(deltas_CGCF), sum(deltas_CGCF)/len(deltas_CGCF)
min_delta_MMSE, max_delta_MMSE, aver_delta_MMSE = min(deltas_MMSE), max(deltas_MMSE), sum(deltas_MMSE)/len(deltas_MMSE)


min_int_delta_CGCF, max_int_delta_CGCF, aver_int_delta_CGCF = min(int_deltas_CGCF), max(int_deltas_CGCF), sum(int_deltas_CGCF)/len(int_deltas_CGCF)
min_int_delta_MMSE, max_int_delta_MMSE, aver_int_delta_MMSE = min(int_deltas_MMSE), max(int_deltas_MMSE), sum(int_deltas_MMSE)/len(int_deltas_MMSE)

min_int_eps_CGCF, max_int_eps_CGCF, aver_int_eps_CGCF = min(int_epss_CGCF), max(int_epss_CGCF), sum(int_epss_CGCF)/len(int_epss_CGCF)
min_int_eps_MMSE, max_int_eps_MMSE, aver_int_eps_MMSE = min(int_epss_MMSE), max(int_epss_MMSE), sum(int_epss_MMSE)/len(int_epss_MMSE)

print(min_delta_CGCF, max_delta_CGCF, aver_delta_CGCF)
print(min_delta_MMSE, max_delta_MMSE, aver_delta_MMSE)
print()
print(100*max_eps_CGCF, 100*aver_eps_CGCF)
print(100*max_eps_MMSE, 100*aver_eps_MMSE)
print()
print()

print(min_int_delta_CGCF, max_int_delta_CGCF, aver_int_delta_CGCF)
print(min_int_delta_MMSE, max_int_delta_MMSE, aver_int_delta_MMSE)
print()
print(100*min_int_eps_CGCF, 100*max_int_eps_CGCF, 100*aver_int_eps_CGCF)
print(100*min_int_eps_MMSE, 100*max_int_eps_MMSE, 100*aver_int_eps_MMSE)