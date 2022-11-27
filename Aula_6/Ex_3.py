# Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores da diagonal principal.

matriz = []

for x in range(5):
    lista = []
    for y in range(5):
        lista.append(int(input("Digite um valor : ")))
    matriz.append(lista)

for x in range (5):
    print(matriz[x][x])