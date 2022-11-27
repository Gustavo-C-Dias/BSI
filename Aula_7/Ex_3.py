# Faça um algoritmo que lê valores para uma matriz M4X4 e um valor para a variável
# “a” (do tipo simples, pode ser: inteiro, float). Multiplicar cada valor contido 
# na matriz pelo valor da variável e colocar os resultados num vetor(lista) V com 
# 16 elementos. Mostre no final o vetor(lista).

from unittest import result


M = 4
a = float(input("Digite o fator multiplicador : "))
matriz = []
resultado = []

for x in range(M):
    list = []
    for y in range(M):
        list.append(int(input(f"Digite o valor para {x}x{y}: ")))
    matriz.append(list)

for x in range(M):
    for y in range(M):
        resultado.append(matriz[x][y] * a)

print(resultado)

