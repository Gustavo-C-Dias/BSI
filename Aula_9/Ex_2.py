# Escreva um algoritmo que leia um valor para X e uma sub-rotina que
# imprima todos os números ímpares do intervalo fechado de 1 a X.

def impar (x):
    if (x == 1):
        print(x)
    else:
        if not(x % 2 == 0):
            impar(x-2)
            print(x)
        else:
            impar(x-1)

numero = int(input("Digite um valor: "))
impar(numero)