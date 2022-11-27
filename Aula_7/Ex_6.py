# Faça um programa que leia um vetor(lista) de 5 posições e uma matriz de 5x5
# calcule e mostre o resultado da multiplicação do primeiro elemento do vetor,
# por toda a primeira linha da matriz, do segundo item do vetor por toda a 
# segunda linha da matriz e assim sucessivamente.

matriz = []
vetor = []
T = 5

for x in range(T):
    list = []
    for y in range(T):
        list.append(int(input(f"Digite o valor para {x}x{y} : ")))
    matriz.append(list)

for x in range(T):
    vetor.append(int(input("Digite o indice do multiplicador : ")))

for x in range(T):
    for y in range(T):
        matriz[x][y] = matriz[x][y] * vetor[x]

print(matriz)