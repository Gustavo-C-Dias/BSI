# Faça um algoritmo que lê estrutura (lista, tupla ou conjunto), 
# K que comporte 20 elementos. Troque a seguir os elementos de índice 
# ímpar com os de índice par imediatamente seguinte mostre no final 
# como ficou a estrutura K, com as alterações.

K = list()
par = 0
impar = 0

for i in range(20):
    K.append(int(input("Digite um número : ")))

for index, valor in enumerate(K):
    if index % 2 == 0 :
        impar = valor
    else :
        par = valor
        K[index-1] = par
        K[index] = impar

print(K)