message = list(input("Введите текст: ").upper())

keys = {
'Б':'З','Ц':'Х','Д':'В','Ф':'Ч','Г':'Т',
'Ш':'С','Ж':'Р','К':'Ч','Л':'П','М':'Н'
}

for index in range(len(message)):
	for key in keys:
		if message[index] == key:
			message[index] = keys[key]
		elif message[index] == keys[key]:
			message[index] = key
		else: pass

print("Зашифрованный текст: ","".join(message))