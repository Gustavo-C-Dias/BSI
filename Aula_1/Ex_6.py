#  linha      quant      c        n
#    1          0        X        X
#    2          0        1        X
#    3 - While
#    4          0        1        10 - User
#    5          0        2        10 
#    6 - if
#    3 - While
#    4          0        2        50 - User
#    5          0        3        50
#    6 - if True
#    7          1        3        50 
#    8 - Terminal: 50
#    3 - While
#    4          1        3        70 - User
#    5          1        4        70
#    6 - if True
#    7          2        4        70
#    8 - Terminal: 70 
#    3 - While 
#    4          2        4        5 - User
#    5          2        5        5
#    6 - if
#    3 - While
#    4          2        5        98 - User
#    5          2        6        98
#    6 - if True
#    7          3        6        98 
#    8 - Terminal: 98

#    9 - Dos 5 números 3 são maiores que 30.

quant = 0
c = 1
while c <= 5:
    n = float(input(f"Digite {c} numero: "))
    c += 1
    if n > 30 :
        quant += 1
        print(n)
    print(c)
    print(quant)

print(f"Numeros acima de 30: {quant}")