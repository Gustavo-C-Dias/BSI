# Faça um algoritmo que receba um valor N correspondente ao tamanho de
# duas matrizes quadradas de ordem N (MNxN). Leia os valores inteiros
# para preencher todas as posições de cada uma das matrizes, e calcule
# a MULTIPLICAÇÃO das matrizes.

N = int(input("Digite o tamanho das matrizes: "))
matriz_1 = []
matriz_2 = []
multiplicacao = []
coluna = 0
d = 0


print("----  Matriz 1  ----")
for x in range(N):
    lista = []
    for y in range(N):
        lista.append(int(input(f"Digite um valor para {x}x{y}: ")))
    matriz_1.append(lista)

print("\n----  Matriz 2  ----")
for x in range(N):
    lista = []
    for y in range(N):
        lista.append(int(input(f"Digite um valor para {x}x{y}: ")))
    matriz_2.append(lista)

for x in range(N): # Linha
    valor = 0
    while d >= (N) :
        print("vezes")
        valor += matriz_1[x][d] * matriz_2[d][coluna]
        if d == N-1:
            d = 0
            coluna += 1
        d = d + 1

    print(valor)