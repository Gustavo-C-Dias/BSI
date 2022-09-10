# Ler um vetor R de 5 elementos, inteiros, contendo o resultado da LOTO.
# A seguir ler um vetor A de 10 elementos inteiros contendo uma aposta.
# A seguir imprima quantos pontos fez o apostador.

R = list()
A = list()
count = 0

for i in range(5):
    R.append(int(input(f"Digite o {i+1} valor da LOTO :")))

print("-------------")

for i in range(10):
    A.append(int(input(f"Digite o {i+1} valor apostado :")))

for y in A:
    for x in R:
       if y == x :
           count += 1

print(f"{count} pontos")