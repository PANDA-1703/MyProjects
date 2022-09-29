# Шифр Цезаря
from concurrent.futures import process

alfavit = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

choice = input("Шифровка/дешифровка (E/D): ").upper()

# Шифровка
def encrypt():
    smeshenie = 4
    fraze = input("Введите слово для шифровки:").lower()
    itog = ''
    for i in fraze:
        location = alfavit.find(i)
        new_location = location + smeshenie
        if i in alfavit:
            itog += alfavit[new_location]
        else:
            itog += i
    print(itog)


# Дешифровка
def decrypt():
    fraze = input("Введите слово для дешифровки:").lower()
    itog = ''
    spisok_itog = []
    for smeshenie in range (0, 33):
        itog = ''
        for i in fraze:
            location = alfavit.find(i)
            new_location = location - smeshenie
            if i in alfavit:
                itog += alfavit[new_location]
            else:
                itog += i
        spisok_itog.append(itog+'\n')      
        smeshenie += 1
    with open("russian.txt") as f:
                for line in f:
                    for smeshenie in range (0,32):
                        if (line == spisok_itog[smeshenie]):
                            print(spisok_itog[smeshenie])
                            return 0
                        else:
                            smeshenie += 1        



def main():
    if choice == "E":
        encrypt()
    elif choice == "D":
        decrypt()
    else:
        print("Ошибка!")
        return 0

main()
