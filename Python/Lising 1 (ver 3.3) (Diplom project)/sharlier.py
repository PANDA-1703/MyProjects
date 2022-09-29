from numpy import*
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Sharlier:
    def __init__ (self, parent, width=400, height=400, title="Шарльер", resizable=(True,True)):
        self.root = Toplevel(parent)
        self.root.title(title)
        #self.root.geometry(f"{width}x{height}")
        #self.root.resizable(resizable[0], resizable[1])

        # Создание entry и вставка нач. данных
        self.R_entry = Entry(self.root)
        self.R_entry.insert(0, 8)
        self.P_entry = Entry(self.root)
        self.P_entry.insert(0, 760)
        self.m_entry = Entry(self.root)
        self.m_entry.insert(0, 500)
        self.ro_air_entry = Entry(self.root)
        self.ro_air_entry.insert(0, 1.29)
        self.ro_gas_entry = Entry(self.root)
        self.ro_gas_entry.insert(0, 0.17)
        self.T_air_entry = Entry(self.root)
        self.T_air_entry.insert(0, 20)
        

        self.draw_widgets()

    def draw_widgets(self): # Отрисовка виджетов
        Label(self.root, text="Введите данные:", bg="#dcd2d5", font="TimesNewRomans 10", anchor=W).grid(row=0, column=0, padx=5, pady=5)
        Label(self.root, width=40, height=2, text="Радиус оболочки:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 1, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Атмосферное давление:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 2, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Масса:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 3, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Плотность воздуха:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 4, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Плотность газа:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 5, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Темература атмосферного воздуха:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 6, column = 0, padx=5)
        

        self.R_entry.grid(row=1, column=1, padx=5)
        self.P_entry.grid(row=2, column=1, padx=5)
        self.m_entry.grid(row=3, column=1, padx=5)
        self.ro_air_entry.grid(row=4, column=1, padx=5)
        self.ro_gas_entry.grid(row=5, column=1, padx=5)
        self.T_air_entry.grid(row=6, column=1, padx=5)
        

        Button(self.root, text="Ok", width=10, command=self.bt_ok).grid(row=7, column=0, padx=10, pady=10)
        Button(self.root, text="Clear", width=10, command=self.clear_entry).grid(row=7, column=1, padx=10, pady=10)

    def clear_entry(self): # Функция очистки полей
        self.R_entry.delete(0, END)
        self.m_entry.delete(0, END)
        self.P_entry.delete(0, END)
        self.ro_air_entry.delete(0, END)
        self.ro_gas_entry.delete(0, END)
        self.T_air_entry.delete(0, END)
        
    
    def bt_ok(self): # Функция основных вычислений
        g = 9.81  # Ускорение свободного падения на земле в м/с^2
        m = double(self.m_entry.get()) # Масса в кг
        R = double(self.R_entry.get())  # Объём оболочки ЛАЛВ в м
        P = double(self.P_entry.get())  # Давление атм. воздуха на уровне моря
        T_air = double(self.T_air_entry.get()) + 273.15 # Температура атмосферного воздуха в К
        ro_air = double(self.ro_air_entry.get())  # Плотность воздуха
        ro_gas = double(self.ro_gas_entry.get())  # Плотность газа
        #T_gas = T_air # Температура газа в К
        #RS_air = 287 # Газов. постоянная воздуха Дж/кг*К
       # RS_gas = 2078 # Газов. постоянная гелия Дж/кг*К
        M_air = 29 # Молекулярная масса воздуха в г/моль
        M_gas = 4
        #RS = 8.314
        a=6.5*10**-3 # Константа, связанная с температурой воздуха в К/м
        b=0.000125 # Константа, связанная с плотностью воздуха в 1/м.
        c=0.4 # Коэффициент лобового сопротивления

        ro_sum=(ro_gas+m)/((4/3)*pi*R**3) # Суммарная плотность материала аэростата, массы гелия и нагрузки
        p1=ro_air/ro_sum # Введенный параметр
        p2=3*c/(8*R) # Введенный параметр
        V=(4/3)*pi*R**3 # Объём 
        M_air = ro_air*V # Молярная масса воздуха в г/моль
        M_gas = ro_gas*V # Молярная масса гелия в г/моль

        # y1 = h, y2 = v
        # Функция графика с учётом температуры
        # Функция двух переменных, первой из которых является список y=[y1,y2], а второй – имя независимой переменной
        def fun(y, t):
                y1, y2= y    
                return [y2,-g+g*p1*exp(-b*y1*T_air/(T_air-a*y1))-p1*p2*exp(-b*y1*T_air/(T_air-a*y1))*y2**2]
        t =arange(0,900,0.01)
        y0 = [0.0,0.0]
        [y1,y2]=odeint(fun, y0,t, full_output=False).T
        plt.title("\n Характеристики  подъёма шарльера \n Объём: %s м^3. Масса : %s кг. \n Подъёмная сила: %s kН. " % (
            round(V, 0), m, round((M_air-M_gas)/22.4, 0)))
        plt.plot(t/60, y1, label='Максимальная высота подъёма: %s км. \n Максимальная скорость: % s м/с .\n С учётом температуры воздуха' %
                (round(max(y1)/1000, 2), round(max(y2), 2)))
        plt.ylabel('Высота в м')
        plt.xlabel(' Время в мин')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()
