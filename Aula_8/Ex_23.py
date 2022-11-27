# Crie uma sub-rotina que receba como parâmetro uma lista V contendo 25 elementos 
# de números inteiros e substitua todos os valores negativos de V por 0. A lista 
# deverá ser retornada para quem realizou a chamada desta função.

def Substituicao(lista):
    for index, valor in enumerate(lista):
        if valor <= 0:
            lista[index] = 0
    return lista

Elementos = []
for x in range(25):
    Elementos.append(int(input(f"Digite um valor para {x} posição: ")))

Elementos = Substituicao(Elementos)
print(Elementos)