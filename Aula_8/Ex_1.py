# Escreva uma função que receba dois números e retorne o maior.

def Maior(a,b):
    if a >= b:
        return a
    else:
        return b

Numero_1 = int(input("Digite um valor: "))
Numero_2 = int(input("Digite um valor: "))

Maior_Num = Maior(Numero_1, Numero_2)
print(f"O maior valor é {Maior_Num}")