# Faça uma sub-rotina que receba como parâmetro uma matriz(lista de lista)
# A[5][5] e retorne a soma de todos os seus elementos.

tamanho = 3
matriz = []

def soma(matriz):
    soma = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            soma += matriz[x][y]
    return soma

for x in range(tamanho):
    aux= []
    for y in range(tamanho):    
        aux.append(int(input(f"Digite um valor para {x}x{y}: ")))
    matriz.append(aux)

valor_soma = soma(matriz)
print(f"O valor da soma dos elementos da matriz é {valor_soma}")
