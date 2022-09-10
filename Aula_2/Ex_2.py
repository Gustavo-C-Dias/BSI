# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine o somatório de todos valores armazenados no vetor.

import numpy as np
soma = 0
vetor = np.array([1,2,3,4,5])

for i in range(5):
    soma += vetor[i]

print(soma)