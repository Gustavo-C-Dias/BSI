# Faça um algoritmo que lê duas listas A e B com 5 elementos cada. Construir uma lista C,
# sendo este a junção das duas outras listas, ou seja, a lista C deverá conter 10 
# elementos. Mostre no final a lista C.

A = [0] * 5
B = [0] * 5
C = []

for i in range(5):
    A[i] = int(input(f"Digite um valor para 1° lista na {i}° posição: "))

print ("\n--------------------\n")

for i in range(5):
    B[i] = int(input(f"Digite um valor para 2° lista na {i}° posição: "))

C += A + B
print(C)

for x in range(len(A)):
    C.append(A[x])

for x in range(len(B)): 
    C.append(B[x])

print(C)