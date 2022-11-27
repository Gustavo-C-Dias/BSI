# Faça um programa que receba 4 valores: I, A, B e C. Desses valores, I é um inteiro
# positivo, A, B e C do tipo reais.

#     a. Suponha que o valor digitado para I seja sempre um valor válido, ou seja
#        1 ou 2 e que os números digitados para A, B e C sejam sempre diferentes 
#        um do outro.

#     b. Escreva os números A, B e C obedecendo a tabela a seguir:
#           1 = Os valores contidos em A, B e C em ordem crescente
#           2 = Os valores contidos em A, B e C em ordem decrescente



I = int(input("Digite 1 ou 2 para executar uma ação: \n 1 - Crescente \n 2 - Decrescente \n"))
if I == 1 or I == 2:
    A = float(input("Digite o valor para A: "))
    B = float(input("Digite o valor para B: "))
    C = float(input("Digite o valor para C: "))
else:
    print("O valor informado para I é invalido")
    
if I == 1:
    if A > B:
        if A > C:
            if B > C:
                print(f"A ordem crescente é: {C}, {B}, {A}")
            else:
                print(f"A ordem crescente é: {B}, {C}, {A}")
        if C > B :
            print (f"A ordem crescente é: {B}, {A}, {C}")
    elif B > C:
        if C > A:
            print(f"A ordem crescnte é {A}, {C}, {B}")
        else:
            print(f"A ordem crescente é: {C}, {A}, {B}")
    elif C > A :                      
        if C > B:
            if B > A:
                print(f"A ordem crescente é: {A}, {B}, {C}")

elif I == 2:
    if A > B:
        if A > C:
            if B > C:
                print(f"A ordem decrescente é: {A}, {B}, {C}")
            else:
                print(f"A ordem decrescente é: {A}, {C}, {B}")
        else :
            print(f"A ordem decrescente é: {C}, {A}, {B}")
    elif C > A :                      
        if C > B:
            if B > A:
                print(f"A ordem decrescente é: {C}, {B}, {A}")
            else:
                print(f"A ordem decrescente é: {C},{A},{B}")
    elif B > C :
        if C > A:
            print(f"A ordem decrescente é {B}, {C}, {A}")
        else:
            print(f"A ordem decrescnte é: {B}, {A}, {C}")