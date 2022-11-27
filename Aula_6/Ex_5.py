# Faça um algoritmo que lê valores para uma matriz M10x10 calcular e mostrar:
#    O somatório dos valores da coluna 2
#    O somatório dos valores da diagonal principal

matriz = []
soma = 0

for x in range(3):
    lista = []
    for y in range(3):
        lista.append(int(input("Digite um valor : ")))
    matriz.append(lista)

for x in range(len(matriz)):
    soma += matriz[x][2]
print(soma)
soma = 0

for x in range (3):
    soma += matriz[x][x]
print(soma)