# Faça um programa que preencha um vetor com 9 números inteiros,
# calcule e mostre os que são números primos e suas respectivas posições.

Lista = list()
cont = 0

for x in range (9):
    aux = int(input(f"Informe o {x} valor : "))
    Lista.append(aux)

print(Lista)

for index, valor in enumerate(Lista):
    for x in range(1,valor):
        if valor % x == 0:
            cont += 1
    if (cont == 1):
        print(f"O numero {valor} ")
    cont = 0