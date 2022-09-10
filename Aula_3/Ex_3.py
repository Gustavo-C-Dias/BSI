# Elabore um algoritmo que leia duas listas de 5 posições, após a leitura realizar a soma
# e imprima o resultado da soma entre as duas listas de inteiros.

lista_1 = [0] * 5
lista_2 = [0] * 5
soma_lista = 0

for i in range(5):
    lista_1[i] = int(input(f"Digite um valor para 1° lista na {i}° posição: "))

print ("\n--------------------\n")

for i in range(5):
    lista_2[i] = int(input(f"Digite um valor para 2° lista na {i}° posição: "))

for i in range(5):
    soma_lista += lista_1[i] + lista_2[i]

print(soma_lista)


# correção

L1 = []
L2 = list()
L3 = []

for x in range(0,5):
    aux = int(input(f"Digite um valor para 1° lista na {i}° posição: "))
    L1.append(aux)
    aux = int(input(f"Digite um valor para 2° lista na {i}° posição: "))
    L2.append(aux)

for x in range(len(L1)):
    aux = L1[x] + L2[x]
    L3.append(aux)

print(L3)
