import math

def nod_fun(x, y): 
    if(y == 0):
        return x  
    else: 
        return nod_fun(y, x % y) 
        
x=int(input("Первое число: ")) 
y =int(input("Второе число: "))   
num = nod_fun(x, y) 
print("Наибольший общий делитель: ", num) 
