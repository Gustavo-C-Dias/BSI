# Faça uma função que inverte uma matriz 10 x 10 (linhas viram colunas e colunas viram linhas).

tamanho = 5
matriz = []

def Inverter (matriz):
    matriz_inversa = []
    for x in range(len(matriz)):
        coluna = []
        for y in range(len(matriz[x])):
            coluna.append(matriz[y][x])
        matriz_inversa.append(coluna)
    return matriz_inversa

for x in range(tamanho):
    aux = []
    for y in range(tamanho):
        aux.append(int(input(f"Digite o valor para posição {x}x{y}: ")))
    matriz.append(aux)

matriz = Inverter(matriz)

for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        print(matriz[x][y], end=" ")
    print()