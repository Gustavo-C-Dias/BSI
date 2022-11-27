# Faça um algoritmo que receba um valor N correspondente ao
# tamanho de uma matriz quadrada de ordem N (MNxN). Calcule
# o DETERMINANTE da matriz

N = int(input("Digite o tamanho da matriz:"))
final_positivo = 0
final_negativo = 0
matriz = []

for x in range(N):
    linha = []
    for y in range(N):
        linha.append(int(input(f"Digite o valor {x}x{y}: ")))
    for x in range(len(linha)-1): 
        linha.append(linha[x])
    matriz.append(linha)

for x in range(N):
    i = N - 1
    diagonal_negativa = 1
    diagonal_positiva = 1
    for y in range(len(matriz)):
        diagonal_positiva = diagonal_positiva * matriz[y][y]
        diagonal_negativa = diagonal_negativa * matriz[i][y]
        i -= 1

    for y in range(len(matriz)):
        del matriz[y][0]
    
    final_positivo += diagonal_positiva
    final_negativo += diagonal_negativa 

determinante = final_positivo - final_negativo
print(determinante)