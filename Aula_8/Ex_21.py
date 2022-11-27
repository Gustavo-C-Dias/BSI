# Elabore um algoritmo que receba as 3 notas de um aluno e uma letra.
# Se a letra for “A”, deve-se chamar uma sub-rotina que deverá calcular
# a média aritmética das notas dos alunos; Se a letra for “P”, deverá 
# calcular a média ponderada, com pesos 5, 3 e 2. A média calculada deverá 
# ser devolvida ao programa principal para, então, ser mostrada.

def Ponderada(a,b,c,):
    return ( (a*5) + (b*3) + (c*2) ) / 10

def Aritmetica(a,b,c):
    return (a + b + c) / 3

def Media (a,b,c,letra):
    if letra == "A":
        return Aritmetica(a,b,c)
    elif letra == "P": 
        return Ponderada(a,b,c)

Nota1 = float(input("Digite uma nota: "))
Nota2 = float(input("Digite uma nota: "))
Nota3 = float(input("Digite uma nota: "))
Letra = input("Digite uma letra: ")

Nota = Media(Nota1,Nota2,Nota3,Letra)
print(f"\nA nota média é: {Nota}") 