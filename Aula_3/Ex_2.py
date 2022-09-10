# Faça um algoritmo que lê 10 valores para uma variável do tipo lista de nome x.
# Após completar toda a leitura da lista, verificar se cada valor armazenado na 
# lista é par ou ímpar. Se for par, fazer com que o valor seja atualizado para o
# resultado da multiplicação do valor contido pelo índice. Se for impar fazer com
# que a lista receba o valor do seu próprio índice.

x = [0] * 10

for i in range(10):
    x[i] = float(input(f"Digite um valor para {i}° posição: "))

for index, valor in enumerate(x):
    if valor % 2 == 0 :
        x[index] = valor * index
    else:   
        x[index] = index

print(x)
