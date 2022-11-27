Estrutura = []
N = 10
cont = 0

for x in range(N):
    Estrutura.append(int(input(f"Digite o {x}º : ")))

for index, valor in enumerate(Estrutura):
    if valor <= 0:
        print(f"{valor} é menor ou igual a 0 e está armazenado na {index}º posição")
        cont += 1

if cont == 0 :
    print("\nNenhum numero menor ou igual a 0 foi informado")