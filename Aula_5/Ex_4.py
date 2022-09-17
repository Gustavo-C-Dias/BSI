# Faça um programa que preencha uma estrutura (lista, tupla ou conjunto)
# com 9 números inteiros, calcule e mostre os números primos e suas 
# respectivas posições na estrutura.

lista = list()
cont = 0

for x in range (9):
    lista.append(int(input("Digite um número: ")))

for i, valor in enumerate(lista):
    for y in range(1, valor):
        if valor % y == 0:
            cont += 1
    if cont == 1 :
        print(f"Valor : {valor}")
        print(f"Posicao : {i} \n")
    cont = 0