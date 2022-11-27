# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine o maior e o menor valor armazenado no vetor.

import numpy as np
vetor = np.array([1,2,8,4,5])
maior = vetor[0]
menor = vetor[0]

for i in range(5):
    if vetor[i] >= maior:
        maior = vetor[i]
    if vetor[i] <= menor:
        menor = vetor[i]

print(f"o menor valor é: {menor}")
print(F"O maior valor é: {maior}")