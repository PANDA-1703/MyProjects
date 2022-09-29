from random import choice, randint
from collections import Counter

text = "High"
symbols = [chr(x) for x in range(65,91)] # A - Z
symbols += [chr(x) for x in range(97,123)] # a - z
# A - z
while True:
	keys = [randint(1,100) for x in range(len(text))]
	k = Counter(keys)
	switch = 0; n = 0
	for l in k:
		if k[keys[n]] > 1:
			switch = 1
			break
		n += 1
	if switch == 0:
		break
keys.sort()
print("keys:",keys)

lattice = [choice(symbols) for x in range(0,101)]

n = 0
for i in range(len(lattice)):
	if n < len(text):
		if i == keys[n]:
			lattice[i] = text[n]
			n += 1
print()

for j in range(0,11):
	if j == 0:
		print(" ", end = "    ")
	else:
		print(j, end = "   ")
print()

n = 0
for j in range(1,len(lattice)):
	if j == 1:
		print(n, end = "  | "); n += 1
		print(lattice[j], end = " | ")
	elif j % 10 != 0:
		print(lattice[j], end = " | ")
	else:
		print(lattice[j], end = " | ")
		print()
		if n < 10:
			print(n, end = "  | "); n += 1
print()