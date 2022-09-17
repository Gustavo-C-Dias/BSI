# Ler uma estrutura (lista, tupla ou conjunto), R de 5 elementos, inteiros,
# contendo o resultado da LOTO. A seguir ler outra estrutura (lista, tupla 
# ou conjunto), A de 10 elementos inteiros contendo uma aposta. A seguir 
# imprima quantos pontos fez o apostador.

resultado = ("1","2","3","4","5")
#resultado = [1,2,3,4,5]
aposta = list()
i = 0

for x in range(10):
    aposta.append(int(input(f"Digite o {x} valor da sequencia de aposta : ")))

for tuple_element in resultado :
    for list_element in aposta :
        if list_element == tuple_element :
            i += 1

print(i)
