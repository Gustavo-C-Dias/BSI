# Construa uma função que receba como parâmetro uma matriz quadrada 4 X 4
# e retorne a soma dos valores da diagonal principal.

def soma_matriz (matriz):
    soma = 0
    for x in range(len(matriz)):
        soma += matriz[x][x]
    return soma

n = int(input("Digite o tamanho da matriz: "))
matriz= []

for x in range(n):
    aux = []
    for y in range(n):
        aux.append(int(input(f"Digite o valor para {x}x{y}: ")))
    matriz.append(aux)

soma = soma_matriz(matriz)
print(soma)
