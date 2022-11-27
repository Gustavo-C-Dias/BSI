Vetor = []
Matriz = []
Linhas = 3
Colunas = 4

for x in range(Linhas):
    Vetor.append(int(input(f"Digite o {x}º valor do vetor : ")))

for x in range(Linhas):
    Vetor_Aux = []
    for y in range(Colunas):
        Vetor_Aux.append(int(input(f"Digite o valor para matriz na posição {x}x{y}: ")))
    Matriz.append(Vetor_Aux)

for x in range(Linhas):
    Matriz[x][1] = Vetor[x]

for linha in Matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()