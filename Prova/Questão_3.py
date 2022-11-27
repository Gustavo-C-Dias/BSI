Estrutura = []
N = 18

for x in range(N):
    Estrutura.append(int(input(f"Digite o {x}º : ")))

Maior = Estrutura[0]
Menor = Estrutura[0]





for index, valor in enumerate(Estrutura):
    if Maior <= valor:
        Maior = valor
        Index_Maior = index
    if Menor >= valor:
        Menor = valor
        Index_Menor = index  

print("--------------------")

print(f"O maior valor é: {Maior}\nEle está na {Index_Maior}º posição\n")
print(f"O menor valor é: {Menor}\nEle está na {Index_Menor}º posição\n")