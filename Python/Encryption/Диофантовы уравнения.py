import math

def nod(m, n):
    return m if n == 0 else nod(n, m % n)
 
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
 
assert c != 0
 
nodAB = nod(abs(a), abs(b))
if c % nodAB:
    print("Невозможно")
else:
    a //= nodAB
    b //= nodAB
    c //= nodAB
 
    for k in range(abs(a)):
        if ( c - b * k ) % a == 0:
            y = k
            x = ( c - b * y ) // a
            print("x =", x, "y =", y)
            break
    else:
        print("Ответа нет")