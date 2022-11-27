# Escreva uma função que receba um número e retorne TRUE se o número for par.

def Par(x):
    return x % 2 == 0

Number = int(input("Digite o valor desejado: "))
print(Par(Number))