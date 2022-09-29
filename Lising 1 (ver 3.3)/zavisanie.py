from numpy import*
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Zavisanie:
    def __init__ (self, parent, width=400, height=400, title="Зависание", resizable=(True,True)):
        self.root = Toplevel(parent)
        self.root.title(title)
    
        self.R_entry = Entry(self.root)
        self.R_entry.insert(0, 8)
        self.m_entry = Entry(self.root)
        self.m_entry.insert(0, 300)

        self.draw_widgets()

    def draw_widgets(self): # Отрисовка виджетов
        Label(self.root, text="Введите данные:", bg="#dcd2d5", font="TimesNewRomans 10", anchor=W).grid(row=0, column=0, padx=5, pady=5)
        Label(self.root, width=40, height=2, text="Радиус оболочки:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 1, column = 0, padx=5)
        Label(self.root, width=40, height=2, text="Масса:", anchor=W, font=("TimesNewRomans", 10, "bold")).grid(row = 3, column = 0, padx=5)

        self.R_entry.grid(row=1, column=1, padx=5)
        self.m_entry.grid(row=3, column=1, padx=5)

        Button(self.root, text="Ok", width=10, command=self.bt_ok).grid(row=6, column=0, padx=10, pady=10)
        Button(self.root, text="Clear", width=10, command=self.clear_entry).grid(row=6, column=1, padx=10, pady=10)

    def clear_entry(self): # Функция очистки полей
        self.R_entry.delete(0, END)
        self.m_entry.delete(0,END)

    def bt_ok(self): # Функция основных вычислений
        g=9.81# ускорение свободного падения на земле в м/с2.
        rv=1.29# плотность атмосферного воздуха в кг/м3.
        rg=0.17# плотность гелия в кг/м3.
        R = double(self.R_entry.get())  # Радиус оболочки ЛАЛВ в м
        mo = double(self.m_entry.get()) # Масса в кг
        b=0.000125# константа, связанная с плотностью воздуха в 1/м
        a=6.5*10**-3# константа, связанная с температурой воздуха в К/м
        c=0.4# коэффициент лобового сопротивления
        V=(4/3)*pi*R**3
        p2=3*c/(8*R)# введенный параметр
        T0=300# температура на уровне моря
        tz=4000# время зависания в секундах
        rgu=1.2# плотность образовавшейся газовой смеси после стравливания гелия в кг/м3 
        
        def fun(y, t):
                y1,y2= y
                if y2<=0:
                        if t<tz:
                                    return [y2,-g+g*(rv/(rg+mo/V))*exp(-b*y1*T0/(T0-a*y1))+(rv/(rg+mo/V))*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]
                        elif t>=tz:
                                return [y2,-g+g*(rv/(rgu+mo/V))*exp(-b*y1*T0/(T0-a*y1))+(rv/(rgu+mo/V))*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]
                else:
                        return [y2,-g+g*(rv/(rg+mo/V))*exp(-b*y1*T0/(T0-a*y1))-(rv/(rg+mo/V))*p2*exp(-b*y1*T0/(T0-a*y1))*y2**2]
        t =arange(0,tz+555,0.1)
        y0 = [0.0,0.0]
        [y1,y2]=odeint(fun, y0,t, full_output=False).T
        plt.title("Подъём, зависание, спуск ЛАЛВ \n с жёсткой оболочкой сферической формы  \n Объём: %s м3. Масса : %s кг. Подъёмная сила: %s kН. "%(round(V,0),mo,round(0.001*g*rv*V,0)))
        plt.plot(t,y1,label='Максимальная высота подъёма: %s км. \n Максимальная скорость: % s м/с .\n Время зависания %s с.'%(round(max(y1)/1000,2), round(max(y2),2),tz-2*555))
        plt.ylabel('Высота в м')
        plt.xlabel(' Время в сек.')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()