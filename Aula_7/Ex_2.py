# Faça um algoritmo que lê uma matriz M10x10. Troque a seguir os valores contidos 
# na linha de índice 2 com os da linha de índice 8 e também troque os valores da 
# linha de índice 5 com os da coluna de índice 9. No final mostre a matriz.


N = 10
matriz = []
list_2 = []
list_8 = []
list_5 = []
coluna_9 = []


for x in range(N):
    list = []
    for y in range(N):
        list.append(int(input(f"Digite o valor para {x}x{y}: ")))
    matriz.append(list)

print()
print()

for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()

print()
print()

for x in range(N):
    list_2.append(matriz[2][x])
    list_8.append(matriz[8][x])
    list_5.append(matriz[5][x]) 
    coluna_9.append(matriz[x][9])

for x in range(N):
    matriz[2][x] = list_8[x]
    matriz[8][x] = list_2[x]
    matriz[5][x] = coluna_9[x]
    matriz[x][9] = list_5[x]

for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()