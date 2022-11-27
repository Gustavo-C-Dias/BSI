# Faça uma sub-rotina que imprima todos os números inteiros de 10 a 1
# (ou seja, em ordem decrescente).

def Decrescente(a,b):
    if a > b:
        for x in range (a,b-1,-1):
            print(x)
    else:
        for x in range (b,a-1,-1):
            print(x)

Numero1 = int(input("Digite um número: "))
Numero2 = int(input("Digite um número: "))
Decrescente(Numero1, Numero2)
