#  Faça um programa que leia três valores inteiros diferentes fornecidos pelo
#  usuário e exiba o valor intermediário entre eles.

valor_1 = int(input("Digite o 1º valor: "))
valor_2 = int(input("Digite o 2º valor: "))
valor_3 = int(input("Digite o 3º valor: "))

if valor_1 >= valor_2 :
    if valor_2 >= valor_3:
        print(f"Intermediario {valor_2}")
    else :
        print(f"Intermediario {valor_3}")
elif valor_2 >= valor_3 :
    if valor_3 >= valor_1 :
        print(f"Intermediario {valor_1}")
    else :
        print(f"Intermediario {valor_3}")
elif valor_3 >= valor_1:
    if valor_1 >= valor_2 :
        print (f"Intermediario {valor_1}")
    else : 
        print(f"Intermediario {valor_2}")