# Escreva um algoritmo que imprima todos os números inteiros de 10 a 1 (em ordem decrescente),
# utilizando recursividade.

def decrescente(n):
    if n > 0:
        print(n)
        decrescente(n-1)

def crescente(n):
    if n > 0:
        decrescente(n-1)
    print(n)

x = 995
decrescente(x)
crescente(x)