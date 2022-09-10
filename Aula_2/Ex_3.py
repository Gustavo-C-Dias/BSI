# Faça um algoritmo que lê 5 valores para uma variável do tipo vetor
# e determine a média de todos valores armazenados no vetor.

import numpy as np
media = 0
vetor = np.array([1,2,3,4,5])

for i in range(5):
    media = media + vetor[i]

media = media / len(vetor)
print(media)