# Escreva um programa que preencha um vetor de inteiros de 10 posições e solicite
# ao usuário um valor inteiro para ser procurado no vetor. Crie uma função que
# receba como parâmetro o vetor e o número a ser procurado. Ao final, retorne quantas
# vezes o número foi encontrado no vetor.

def procura (lista, valor):
    vezes = 0
    for x in lista:
        if x == valor:
            vezes += 1
    return vezes

tamanho = int(input("Digite o tamanho do vetor: "))
lista = []

for x in range(tamanho):
    lista.append(int(input(f"Digite um valor para {x} posição: ")))

valor_busca = int(input("Digite o valor a ser procurado: "))

vezes = procura(lista,valor_busca)

print(id(lista))

print("-" * 35)
print(f"O valor {valor_busca} foi encontrado {vezes} vezes")