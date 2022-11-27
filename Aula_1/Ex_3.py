# Faça um programa que leia uma quantidade indeterminada de números positivos
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], 
# [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido 
# um número negativo. 

cont_0 = 0
cont_26 = 0
cont_51 = 0
cont_76 = 0

while True:
    numero = int(input("Digite um número: "))
    if numero >= 0 and numero <= 25 :
        cont_0 += 1
    elif numero >= 26 and numero <= 50 :
        cont_26 += 1
    elif numero >= 51 and numero <= 75 :
        cont_51 += 1
    elif numero >= 76 and numero <= 100 :
        cont_76 += 1
    elif numero <= 0 :
        print("\n\nDigitou um numero negativo\n\n")
        break
    elif numero > 100 :
        print("Digite um valor valido (0 - 100)")
    
print (f"Número entre 0 - 25: {cont_0}")
print (f"Número entre 26 - 50: {cont_26}")
print (f"Número entre 51 - 75: {cont_51}")
print (f"Número entre 76 - 100: {cont_76}")