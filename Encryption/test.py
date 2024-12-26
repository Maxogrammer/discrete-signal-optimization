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

x0 = 0.0674
y0 = 0.0674
z0 = 0.0676
w0 = 0.067

x = x0
y = y0
z = z0
w = w0

delta = 0.0001

K = 5

for k in range(K):
	n_old = 0

	while n_old < 27:
		n = 0
		a = (x+y+z+w+1) * 50 / (k+1)

		for i in range(len(new_data)):
			cur = new_data[i]

			sum1 = cur['O']*x+cur['I']*y+cur['&']*z+cur['@']*w - cur['p']
			if abs(sum1) <= a:
				n += 1

		if n < n_old:		
			x = x0
			y = y0
			z = z0
			w = w0
		
		else:
			n_old = n

			x0 = x
			y0 = y
			z0 = z
			w0 = w

		x = x0 + random()*delta
		y = y0 + random()*delta
		z = z0 + random()*delta
		w = w0 + random()*delta

	print(k)

print(x)
print(y)
print(z)
print(w)
