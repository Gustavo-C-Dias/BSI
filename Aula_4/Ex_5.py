# Faça um programa que preencha dois vetores de dez elementos numéricos
# cada um e mostre o vetor resultante da intercalação deles:

L1 = list()
L2 = list()
L3 = list()

for x in range(10):
    L1.append(int(input(f"Digite o {x} valor para 1º lista : ")))

print("\n ------------ \n")

for x in range(10):
    L2.append(int(input(f"Digite o {x} valor para 2º lista : ")))

for x in range(len(L1)):
    L3.append (L1[x])
    L3.append (L2[x])

print(L3)