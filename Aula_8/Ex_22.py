# Faça um algoritmo contendo uma sub-rotina que receba dois números positivos 
# inteiros por parâmetro e retorne a soma dos N números inteiros existentes 
# entre eles, incluindo na soma os dois números informados.

def Soma (a,b):
    valor = 0
    if a <= b:
        for x in range(a,b+1):
            valor += x
    else:
        for x in range(b,a+1):
            valor += x
    return valor

A = int(input("Digite um valor: "))
B = int(input("Digite um valor: "))
Soma_final = Soma(A,B)
print(Soma_final)