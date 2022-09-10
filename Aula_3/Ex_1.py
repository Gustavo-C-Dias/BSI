# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x e mostre os 10 valores armazenados.

x = [0] * 10

for i in range(10):
    x[i] = input("Digite um valor:")

print(x)
