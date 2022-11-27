# Crie uma sub-rotina que receba como parâmetro um vetor V[25] de números
# inteiros e substitua todos os valores negativos de A por 0. O vetor deverá
# ser mostrado no programa principal.

tamanho = 5
A = []

def substituir(A):
    for x in range(len(A)):
        if A[x] < 0:
            A[x] = 0

for x in range(tamanho):
    A.append(int(input(f"Digite o valor para {x}: ")))

substituir(A)
print(A)
