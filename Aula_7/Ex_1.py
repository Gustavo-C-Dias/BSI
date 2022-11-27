# Faça um algoritmo que receba um valor N correspondente ao tamanho de duas
# matrizes quadradas de ordem N (M NxN). Leia os valores inteiros para preencher 
# todas as posições de cada uma das matrizes, e calcule a SOMA das matrizes.

import numpy as np

N = int(input("Digite o tamanho da matriz : "))
matriz_1 = []
matriz_2 = []
matriz_resultado = np.zeros((N,N))


for x in range(N):
    list = []
    for y in range(N):
        list.append(int(input(f"Digite o valor para {x}x{y}: ")))
    matriz_1.append(list)

print("\n----------\n")

for x in range(N):
    list = []
    for y in range(N):
        list.append(int(input(f"Digite o valor para {x}x{y}: ")))
    matriz_2.append(list)

for x in range(N):
    for y in range(N):
        matriz_resultado[x][y] = matriz_1[x][y] + matriz_2[x][y]

for lista in matriz_resultado:
    for elemento in lista:
        print(elemento, end=' ')
    print()




