# Faça um algoritmo que lê uma matriz M5x5. Calcular e mostrar a soma de todos os valores da linha 4.

matriz = []
soma = 0

for x in range(5):
    lista = []
    for y in range(5):
        lista.append(int(input("Digite um valor : ")))
    matriz.append(lista)

for x in range(len(matriz[4])):
    soma += matriz[4][x]

print(soma) 
