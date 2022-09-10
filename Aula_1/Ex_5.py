# Faça um programa que receba um valor inteiro fornecido pelo usuário
# e imprima a sequência de Fibonacci até este número. A série de Fibonacci 
# é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 

valor_fibonacci = int(input("Digite um valor inteiro para sequencia Fibonacci: "))
num_anterior = 0
resultado = 0
x = 1

while x <= valor_fibonacci:
        resultado = num_anterior + x
        num_anterior = x
        x = resultado
        print (num_anterior)
