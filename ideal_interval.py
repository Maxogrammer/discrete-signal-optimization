from random import randint

def fun(n):
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

n = 100

data = {}
total = 0
numbers = []
for i in range(n):
    number = randint(30, 180)
    numbers.append(number)
    factors = fun(number)
    for j in factors:
        total += 1

        try:
            data[j] += 1
        except:
            data[j] = 1

sum_tmp = 0
for key in list(data.keys()):
    sum_tmp += key*data[key]

res = sum_tmp / total
print(res)

print([i/res for i in numbers])
