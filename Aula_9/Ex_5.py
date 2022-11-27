# Faça uma sub-rotina que verifique se a matriz informada é simétrica ou não.
# Uma matriz só pode ser considerada simétrica se A[ i, j ] = A [ j, i ].

Linha = int(input("Digite o tamanho da linha: "))
Coluna = int(input("Digite o tamanho da coluna: "))
Matriz = []

def Simetrica (matriz):
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if not(matriz[x][y] == matriz[y][x]):
                return False
    return True

for x in range(Linha):
    Aux = []
    for y in range(Coluna):
        Aux.append(int(input(f"Digite o valor para posição {x}x{y}: ")))
    Matriz.append(Aux)

Matriz_Simetrica = Simetrica(Matriz)

if Matriz_Simetrica:
    print("\nMatriz Simétrica")
else:
    print("\nMatriz Assimétrica")
