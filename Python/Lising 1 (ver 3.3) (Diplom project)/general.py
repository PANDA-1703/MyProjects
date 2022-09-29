from numpy import*
from scipy.integrate import odeint
from scipy.integrate import ode
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class General:
    def __init__ (self, parent, width=400, height=400, title="Общее", resizable=(True,True)):
        self.root = Toplevel(parent)
        self.root.title(title)
        #self.root.geometry(f"{width}x{height}")
        #self.root.resizable(resizable[0], resizable[1])

        # Создание entry и вставка нач. данных
        self.r_entry = Entry(self.root)
        self.r_entry.insert(0, 8)
        self.m_entry = Entry(self.root)
        self.m_entry.insert(0, 500)
        self.plAtm_entry = Entry(self.root)
        self.plAtm_entry.insert(0, 1.2)
        self.plGel_entry = Entry(self.root)
        self.plGel_entry.insert(0, 0.18)
        self.t_entry = Entry(self.root)
        self.t_entry.insert(0, 20)

        self.draw_widgets()

    def draw_widgets(self): # Отрисовка виджетов
        Label(self.root, text="Введите данные:", bg="#dcd2d5", font="TimesNewRomans 10", anchor=W).grid(row=0, column=0, padx=5, pady=5)
        Label(self.root, width=40, height=2, text="Радиус оболочки:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 1, column = 0, padx=5)
        #Entry(self.root, width=20).grid(row=1, column=1)
        Label(self.root, width=40, height=2, text="Масса:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 2, column = 0, padx=5)
        #Entry(self.root, width=20).grid(row=2, column=1)
        Label(self.root, width=40, height=2, text="Плотность воздуха:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 3, column = 0, padx=5)
        #Entry(self.root, width=20).grid(row=3, column=1)
        Label(self.root, width=40, height=2, text="Плотность газа:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 4, column = 0, padx=5)
        #Entry(self.root, width=20).grid(row=4, column=1)
        Label(self.root, width=40, height=2, text="Температура воздуха:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 5, column = 0, padx=5)
        #Entry(self.root, width=20).grid(row=5, column=1)

        self.r_entry.grid(row=1, column=1, padx=5)
        self.m_entry.grid(row=2, column=1, padx=5)
        self.plAtm_entry.grid(row=3, column=1, padx=5)
        self.plGel_entry.grid(row=4, column=1, padx=5)
        self.t_entry.grid(row=5, column=1, padx=5)

        Button(self.root, text="Ok", width=10, command=self.bt_ok).grid(row=6, column=0, padx=10, pady=10)
        Button(self.root, text="Clear", width=10, command=self.clear_entry).grid(row=6, column=1, padx=10, pady=10)

    def clear_entry(self): # Функция очистки полей
        self.r_entry.delete(0, END)
        self.m_entry.delete(0, END)
        self.plAtm_entry.delete(0, END)
        self.plGel_entry.delete(0, END)
        self.t_entry.delete(0, END)
    
    def bt_ok(self): # Функция основных вычислений
        g = 9.81  # Ускорение свободного падения на земле в м/с^2
        R = double(self.r_entry.get())  # Радиус оболочки ЛАЛВ в м
        rv = double(self.plAtm_entry.get())  # Плотность атмосферного воздуха в кг/м^3
        rg = double(self.plGel_entry.get())  # Плотность гелия в кг/м^3
        b = 0.000128  # Константа, связанная с плотностью воздуха в 1/м
        a = 6.5*10**-3  # Константа, связанная с температурой воздуха в К/м
        c = 0.4  # Коэффициент лобового сопротивления
        m = double(self.m_entry.get())  # Масса в кг
        V = (4/3)*pi*R**3  # Объём
        rs = rg+m/V  # Суммарная плотность материала ЛАЛВ, массы гелия, и нагрузки
        p1 = rv/rs  # Введенный параметр
        p2 = 3*c/(8*R)  # Введенный параметр
        T0 = double(self.t_entry.get()) + 273.15  # Температура в К

        # y1 = h, y2 = v
        # Функция графика с учётом температуры
        # Функция двух переменных, первой из которых является список y=[y1,y2], а второй – имя независимой переменной
        
        def fun(y, t): # Функция двух переменных, первой из которых является список y=[y1,y2], а второй – имя независимой переменной
            y1, y2 = y
            return [y2, -g+g*p1*exp(-b*y1*T0/(T0-a*y1))-p1*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]

        # Массив с равномерно разнесенными значениями внутри заданного интервала
        t = arange(0, 700, 0.01) # Одномерный массив от 0 до 1100 с шагом 0.01
        y0 = [0.0, 0.0]
        # odeint() - предназначена для решения систем обыкновенных дифференциальных уравнений первого порядка с начальными условиями в одной точке (задача Коши)
        [y1, y2] = odeint(fun, y0, t, full_output=False).T 

        plt.title("\n Характеристики  подъёма ЛАЛВ  \n Объём: %s м^3. Масса : %s кг. \n Подъёмная сила: %s kН. " % (
            round(V, 0), m, round(0.001*g*rv*V, 0)))
        plt.plot(t/60, y1, label='Максимальная высота подъёма: %s км. \n Максимальная скорость: % s м/с .\n С учётом температуры воздуха' %
                (round(max(y1)/1000, 2), round(max(y2), 2)))
        # Функция графика без учёта температуры
        def fun(y, t):
            y1, y2 = y
            return [y2, -g+g*p1*exp(-b*y1)-p1*p2*exp(-b*y1)*y2**2] 
        [y1, y2] = odeint(fun, y0, t, full_output=False).T
        plt.plot(t/60, y1, label='Максимальная высота подъёма: %s км. \n Максимальная скорость: % s м/с \n Без учёта температуры воздуха' % (round(max(y1)/1000, 2), round(max(y2), 2)))
        plt.ylabel('Высота в м')
        plt.xlabel('Время в минутах')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()