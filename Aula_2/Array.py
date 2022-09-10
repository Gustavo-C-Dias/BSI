# Array = estruturas de dados que permite armazenar mais de um valor. Identificação para saber qual é
# atravez dos index. Estrutura homogêneas para valores numericos (int, float, ...)  

# 
import numpy as np

vetor = np.zeros(10)
print(type(vetor))
print(vetor)


for i in range(10):
    vetor[i] = i 
print(type(vetor))
print(vetor)


vetor = [1,2,3,4,5]
print(type(vetor))
print(vetor)


vetor = np.array([1,2,3,4,5])
print(type(vetor))
print(vetor)


# Matriz
vetor = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(type(vetor))
print(vetor)


#Metodos especiais
vetor.sum() # - soma total da estrutura
vetor.mean()# - média da estrutura
vetor.std()# - desvio padrão
vetor.max()# - maior valor
vetor.min()# - menor valor
vetor.argmax()# - retorna a posição do maior valor
vetor.argmin()# - retorna a posição do menor valor

