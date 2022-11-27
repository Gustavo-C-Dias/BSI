N = 5
Matriz = []

for x in range(N):
    Vetor_Aux = []
    for y in range(N):
        Vetor_Aux.append(int(input(f"Digite o valor para matriz na posição {x}x{y}: ")))
    Matriz.append(Vetor_Aux)

Maior = Matriz[0][0]
for x in range(len(Matriz)):
    for y in range(len(Matriz)):
        if Maior <= Matriz[x][y]:
            Maior = Matriz[x][y]
            Index_Linha = x

Menor = Matriz[Index_Linha][0]
for y in range(len(Matriz[Index_Linha])):
    if Menor >= Matriz[Index_Linha][y]:
        Menor = Matriz[Index_Linha][y]

print(f"O minimax da matriz é : {Menor}")