# Faça um algoritmo que lê 10 valores para uma variável do tipo vetor
# e mostre qual a posição está armazenado o maior e o menor valor no vetor.

import numpy as np

vetor = np.zeros(10)

for i in range(10):
    vetor[i] = float(input(f"Digite o {i}º valor: ")) 

maior_valor = vetor[0]
menor_valor = vetor[0]
maior_indice = 0
menor_indice = 0

for i in range(10):
    if vetor[i] >= maior_valor:
        maior_valor = vetor[i]
        maior_indice = i
    if vetor[i] <= menor_valor:
        menor_valor = vetor[i]
        menor_indice = i

print(f"O menor valor estã na posição: {menor_indice}")
print(f"O maior valor estã na posição: {maior_indice}")
