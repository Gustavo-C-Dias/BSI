# Faça um programa que preencha dois vetores, X e Y, com dez 
# números inteiros cada. Calcule e mostre os seguintes vetores resultantes:
# A diferença entre X e Y

X = list()
Y = list()
Semelhante = list()
Diferenca = list()
cont = 0

for x in range (10):
    X.append(int(input(f"{x+1} numero para 1º lista :")))

print("------------")

for x in range (10):
    Y.append(int(input(f"{x+1} numero para 2º lista :")))

for index_x in range(len(X)):
    for index_y in  range(len(Y)):
        if (X[index_x] == Y [index_y]):
            Semelhante.append(X[index_x])

for index_x in range(len(X)):
    for i in range(len(Semelhante)):
        if(Semelhante[i] == X[index_x]):
            cont += 1
    if (cont == 0):
        Diferenca.append(X[index_x])
    cont = 0

print(f"\n{Diferenca}")
