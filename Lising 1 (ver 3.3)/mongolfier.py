from numpy import*
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox


class Mongolfier:
    def __init__ (self, parent, width=400, height=400, title="Монгольфьер", resizable=(True,True)):
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
        self.T_atm_entry = Entry(self.root)
        self.T_atm_entry.insert(0, 20)
        self.T_shell_entry = Entry(self.root)
        self.T_shell_entry.insert(0, 90)

        self.draw_widgets()

    def draw_widgets(self): # Отрисовка виджетов
        Label(self.root, text="Введите данные:", bg="#dcd2d5", font="TimesNewRomans 10", anchor=W).grid(row=0, column=0, padx=5, pady=5)
        Label(self.root, width=40, height=2, text="Радиус оболочки:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 1, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Атмосферное давление:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 2, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Масса:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 3, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Темература атмосферного воздуха:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 4, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Температура воздуха в оболочке шара:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 5, column = 0, padx=5)
        

        self.R_entry.grid(row=1, column=1, padx=5)
        self.P_entry.grid(row=2, column=1, padx=5)
        self.m_entry.grid(row=3, column=1, padx=5)
        self.T_atm_entry.grid(row=4, column=1, padx=5)
        self.T_shell_entry.grid(row=5, column=1, padx=5)

        Button(self.root, text="Ok", width=10, command=self.bt_ok).grid(row=6, column=0, padx=10, pady=10)
        Button(self.root, text="Clear", width=10, command=self.clear_entry).grid(row=6, column=1, padx=10, pady=10)

    def clear_entry(self): # Функция очистки полей
        self.R_entry.delete(0, END)
        self.P_entry.delete(0, END)
        self.m_entry.delete(0,END)
        self.T_atm_entry.delete(0, END)
        self.T_shell_entry.delete(0, END)
    
    def bt_ok(self): # Функция основных вычислений
        g = 9.81  # Ускорение свободного падения на земле в м/с^2
        R = double(self.R_entry.get())  # Радиус оболочки ЛАЛВ в м
        m = double(self.m_entry.get()) # Масса в кг
        P = double(self.P_entry.get())  # Давление атм. воздуха на уровне моря
        T_atm = double(self.T_atm_entry.get()) + 273.15 # Температура атмосферного воздуха
        T_shell = double(self.T_shell_entry.get()) + 273.15 # Температура воздуха в оболочке шара
        RS = 8.31  # Универсальная газовая постоянная воздуха в Дж/кг*град
        M = 29 # Молярная масса воздуха в г/моль
        ro_air = 1.2  # Температура атмосферного воздуха в К
        ro_gas = 0.9  # Температура газа в К
        V=(4/3)*pi*R**3 # Объём 
        ro_sum=(ro_gas+m)/V # Суммарная плотность материала стратостата, массы горячего воздуха и нагрузки
        a=6.5*10**-3 # Константа, связанная с температурой воздуха в К/м
        b=0.000125 # Константа, связанная с плотностью воздуха в 1/м.
        c=0.4 # Коэффициент лобового сопротивления
        p1=ro_air/ro_sum # Введенный параметр
        p2=3*c/(8*R) # Введенный параметр
        
        F = 0.465*P*(1/(T_atm-273.15)-1/(T_shell-273.15)) # Подъёмная сила
        
        

        # y1 = h, y2 = v
        # Функция графика с учётом температуры
        # Функция двух переменных, первой из которых является список y=[y1,y2], а второй – имя независимой переменной
        def fun(y, t):
                y1, y2= y    
                return [y2,-g+g*p1*exp(-b*y1*T_atm/(T_atm-a*y1))-p1*p2*exp(-b*y1*T_atm/(T_atm-a*y1))*y2**2]
        t =arange(0,900,0.01)
        y0 = [0.0,0.0]
        [y1,y2]=odeint(fun, y0,t, full_output=False).T
        plt.title("\n Характеристики  подъёма монгольфьера  \n Объём: %s м^3. Масса : %s кг. \n Подъёмная сила: %s kН." % (
            round(V, 0), m, round(F, 0)))
        plt.plot(t/60, y1, label='Максимальная высота подъёма: %s км. \n Максимальная скорость: % s м/с .\n С учётом температуры воздуха' %
                (round(max(y1)/1000, 2), round(max(y2), 2)))
        plt.ylabel('Высота в м')
        plt.xlabel(' Время в мин')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()



    # def grab_focus(self): #Фокусировка
    #     self.root.grab_set()
    #     self.root.focus_set()
    #     self.root.wait_window()
