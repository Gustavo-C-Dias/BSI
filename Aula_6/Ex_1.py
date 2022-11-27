# Faça um algoritmo que lê uma matriz M5x5 e mostrar os valores digitados para a matriz M.

matriz = []

for x in range(5):
    lista = []
    for y in range(5):
        lista.append(int(input("Digite um valor : ")))
    matriz.append(lista)

for x in matriz:
    for y in x:
        print(y, end =' ')
    print()

print(matriz)