# Altere o algoritmo anterior para que ele realize o produto da primeira lista, pelo inverso da segunda lista.

lista_1 = [0] * 5
lista_2 = [0] * 5
produto = []

for i in range(5):
    lista_1[i] = int(input(f"Digite um valor para 1° lista na {i}° posição: "))

print ("\n--------------------\n")

for i in range(5):
    lista_2[i] = int(input(f"Digite um valor para 2° lista na {i}° posição: "))

for i in range(5):
    produto.append(lista_1[i] * lista_2[len(lista_2) -i -1])

print(produto)
    
     