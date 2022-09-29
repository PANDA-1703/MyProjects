from numpy import*
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from mongolfier import Mongolfier
from sharlier import Sharlier
from stratostat import Stratostat
from general import General
from zavisanie import Zavisanie

# Стартовое окно. Выбор ЛАВЛ
class Window:
    def __init__ (self, width=400, height=400, title="Выбор ЛАВЛ", resizable=(True,True)):
        self.root = Tk()
        self.root.title(title)
        #self.root.geometry(f"{width}x{height}") # Задать размер окна
        #self.root.resizable(resizable[0], resizable[1])

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self): # Отрисовка виджетов
        Label(self.root, text="Выберите летательный аппарат", bg="#dcd2d5", font="TimesNewRomans 12").grid(row=0, column=0)

        Button(self.root, width=25, height=4, text="Монгольфьер", relief=GROOVE, bg="#0cd314", font=("TimesNewRomans", 12, "bold"), command = self.create_mong).grid(row=1, column=0)
        Button(self.root, width=25, height=4, text="Шарльер", relief=GROOVE, bg="#0bb712", font=("TimesNewRomans", 12, "bold"), command = self.create_sharl).grid(row=2, column=0)
        Button(self.root, width=25, height=4, text="Стратостат", relief=GROOVE, bg="#098a0e", font=("TimesNewRomans", 12, "bold"), command = self.create_stratost).grid(row=3, column=0)
        Button(self.root, width=25, height=4, text="Модификация", relief=GROOVE, bg="#f06637", font=("TimesNewRomans", 12, "bold"), command = self.create_general).grid(row=4, column=0)
        Button(self.root, width=25, height=4, text="Зависание", relief=GROOVE, bg="#cb491c", font=("TimesNewRomans", 12, "bold"), command = self.create_zavisanie).grid(row=5, column=0)

    def create_mong(self, width=400, height=400, title="Монгольфьер", resizable=(True, True)):
        Mongolfier(self.root, width, height, title, resizable)

    def create_sharl(self, width=400, height=400, title="Шарльер", resizable=(True, True)):
        Sharlier(self.root, width, height, title, resizable)
    
    def create_stratost(self, width=400, height=400, title="Стратостат", resizable=(True, True)):
        Stratostat(self.root, width, height, title, resizable)

    def create_general(self, width=400, height=400, title="Модификация", resizable=(True, True)):
        General(self.root, width, height, title, resizable)

    def create_zavisanie(self, width=400, height=400, title="Зависание", resizable=(True, True)):
        Zavisanie(self.root, width, height, title, resizable)
    


if __name__ == "__main__":
    win = Window()
    win.run()