# Escreva uma função que receba a base e a altura de um triângulo e retorne a sua área (A = (base x altura)/2).

def Area_Triangulo (base, altura):
    Area = base * altura / 2
    return Area

Base = int(input("Digite o valor da base: "))
Altura = int(input("Digite o valor da altura: "))
Area = Area_Triangulo(Base, Altura)
print(f"A area do triangulo de base = {Base} e altura = {Altura} tem uma area de {Area}")