import math

def vvod():
    print("Введите стартовое время участника(hh mm ss):")
    h1 = int(input("Часы: "))
    m1 = int(input("Минуты: "))
    s1 = int(input("Секунды: "))
    print("Введите время финиша участника(hh mm ss):")
    h2 = int(input("Часы: "))
    m2 = int(input("Минуты: "))
    s2 = int(input("Секунды: "))
    if (h1 < 0 or m1<0 or s1<0 or h2<0 or m2<0 or s2<0):
        print("Данные должны быть больше 0!")
        return 0

    # Сам алгоритм
    start_time = s1 + m1*60 + h1*3600 # переводим всё в секунды
    finish_time = s2 + m2*60 + h2*3600

    if (finish_time <= start_time):
        print("Время финиша меньше времени старта")
        return 0 

    result = finish_time - start_time # время результата в секундах
    res_h = result // 3600  # обратное преобразование в hh:mm:ss
    res_m = (result % 3600) // 60
    res_s = result % 60
    print("Время участника: ", res_h, ":", res_m, ":",res_s)

vvod()
