# Faça uma sub-rotina que recebe duas listas A e B com dez elementos
# inteiros como parâmetro. A sub-rotina deverá determinar e mostrar
# o vetor C que contém os elementos que estão em A, mas que não estão
# em B. A lista C deverá ser mostrada no programa principal.

A = []
B = []
C = []
tamanho = 5

def itens_comum (A,B):
    for x in range(len(A)):
        cont = 0
        for y in range(len(B)):
            if(A[x] == B[y]):
                cont += 1
        if cont == 0:
            C.append(A[x])

for x in range(tamanho):
    A.append(int(input("Digite um valor para A: ")))

for x in range(tamanho):
    B.append(int(input("Digite um valor para B: ")))

itens_comum(A,B)
print(f"Os elementos que pertecem apenas em A são {C}")