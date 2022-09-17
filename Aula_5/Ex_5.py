# Faça um programa que preencha duas estruturas (lista, tupla ou conjunto), 
# X e Y, com dez números inteiros cada. Calcule e mostre os seguintes o 
# seguinte resultado:

X = set()
Y = set()

for i in range(10):
    X.add(int(input("Digite um valor :")))
print("\n---------\n")
for i in range(10):
    Y.add(int(input("Digite um valor :")))

print(X - Y)
