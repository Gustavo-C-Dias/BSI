# Faça um algoritmo que lê uma matriz M2X2 que calcula e mostra o resultado do determinante desta matriz.

M = 2
matriz = []
diagonal_positiva = 1
diagonal_negativa = 1
determinante = 0
i = M - 1

for x in range(M):
    list = []
    for y in range(M):
        list.append(int(input(f'Digite o valor para {x}x{y} : ')))
    matriz.append(list)

for x in range(M):
    diagonal_positiva = diagonal_positiva * matriz[x][x]
    diagonal_negativa = diagonal_negativa * matriz[x][i]
    i -= 1

determinante = diagonal_positiva - diagonal_negativa
print(determinante)