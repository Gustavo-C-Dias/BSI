# Faça um algoritmo que lê uma matriz M5X5 e crie 2 vetores(listas) 
# SL (soma das linhas) e SC (soma das colunas) com 5 posições cada.
# Adicionar aos vetores o resultado da soma das linhas e das colunas 
# da matriz, no final mostrar os dois vetores.

M = 3
matriz = []
SL = []
SC = []

for x in range(M):
    list = []
    for y in range(M):
        list.append(int(input(f"Digitar valor da posição {x}x{y} :")))
    matriz.append(list)

for x in range(M):
    soma_linha = 0
    soma_coluna = 0
    for y in range(M):
        soma_linha += matriz[x][y]
        soma_coluna += matriz[y][x]
    SL.append(soma_linha)
    SC.append(soma_coluna)

for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()

print(f"Soma das linhas {SL}")
print(f"Soma das colunas {SC}")