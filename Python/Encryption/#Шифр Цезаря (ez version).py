#Шифр Цезаря

alfavit = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
smeshenie = 4

choice = input("Шифровка/дешифровка (E/D): ").upper()

#Шифровка
def encrypt():
    fraze = input("Введите слово для шифровки:").upper()
    itog = ''
    for i in fraze:
        location = alfavit.find(i)
        new_location = location + smeshenie
        if i in alfavit:
            itog += alfavit[new_location]
        else:
            itog += i
    print(itog)    

#Дешифровка
def decrypt():
    fraze = input("Введите слово для дешифровки:").upper()
    itog = ''
    for i in fraze:
        location = alfavit.find(i)
        new_location = location - smeshenie
        if i in alfavit:
            itog += alfavit[new_location]
        else:
            itog += i
    print(itog)


def main():     
    if choice == "E":               
        encrypt()
    elif choice == "D":
        decrypt()
    else:
        print("Ошибка!")
        return 0  

main()
