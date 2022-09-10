# Faça um programa que preencha um vetor com os modelos de cinco carros
# (exemplos de modelos: Fusca, Gol, Vectra, etc). Carregue outro vetor
# com o consumo desses carros, isto é, quantos quilômetros cada um deles
# faz com um litro de combustível. Calcule e mostre:
#      a - O modelo do carro mais econômico; e 
#      b - Quantos litros de combustível cada um dos carros cadastrados 
#          consome para percorrer uma distância de 1000 Km.


Modelo = list()
Consumo = list()

for x in range(5):
    Modelo.append(input(f"\n Digite o modelo do veiculo : "))
    Consumo.append(float(input(f"Digite o consumo do {Modelo[x]} : ")))

print("\n ------------ \n")

Carro_eco = Consumo[0]
for x in range(len(Consumo)):
    if (Carro_eco <= Consumo[x]):
        index_eco = x
print(f"O modelo {Modelo[index_eco]} é o mais economico com {Consumo[index_eco]} km/L")

print("\n ------------ \n")

for x in range(len(Consumo)):
    litro_gasto = 1000 / Consumo[x] 
    print(f"\nModelo :{Modelo[x]}")
    print(f"Consumo Km/L :{Consumo[x]}")
    print(f"Gasto 1000Km :{litro_gasto}")