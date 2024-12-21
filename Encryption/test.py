from sys import path as syspath
from os import path as ospath
from random import random

import json

syspath.append('./')

current_directory = ospath.dirname(__file__)
data_path = ospath.join(current_directory, ".." , 'Data', 'PreparedExp', 'Phone1.json')

with open(data_path, "r") as file:
	full_data = json.load(file)

new_data = []

for i in range(len(full_data)):
	new_data.append({'O': 0, 'I': 0, '@': 0, '&': 0, 'p': 0})
	cycle = full_data[i]
	new_data[i]['p'] = cycle[0][0] - cycle[0][1]
	for j in cycle[1:]:
		symbol = j[1]
		num = j[0]

		new_data[i][symbol] = new_data[i][symbol] + num

x = 0.0675
y = 0.0676
z = 0.0674
w = 0.0674

n = 0
n_old = 0
delta = 0.00000001

divisor = 2
K = 100000000
for k in range(K):
	while n <= 27:
		a = (x+y+z+w+1) / (divisor**(k+1))

		for i in range(len(new_data)):
			cur = new_data[i]

			sum1 = cur['O']*x+cur['I']*y+cur['&']*z+cur['@']*w - cur['p']
			if abs(sum1) <= a:
				n += 1

		if n_old <= n:		
			x0 = x
			y0 = y
			z0 = z
			w0 = w

			x = x + random()*delta
			y = y + random()*delta
			z = z + random()*delta
			w = w + random()*delta
		
		else:
			x = x0 + random()*delta
			y = y0 + random()*delta
			z = z0 + random()*delta
			w = w0 + random()*delta

print(x)
print(y)
print(z)
print(w)
