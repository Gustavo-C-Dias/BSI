# Escreva uma função que receba o lado de um quadrado e retorne a sua área (A = lado²).

def Area (x):
    return x ** 2

Lado = int(input("Digite o valor do lado: "))
Area_valor = Area(Lado)
print(f"A área do triangulo de tamanho {Lado} é {Area_valor}")