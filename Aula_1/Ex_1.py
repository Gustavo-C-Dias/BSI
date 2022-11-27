# Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura
# do degrau e a altura que o usuário deseja alcançar subindo a escada, calcule e 
# mostre quantos degraus ele deverá subir para atingir seu objetivo. Todas as medidas
# fornecidas devem estar em metros.

altura = float(input("Digite o valor da altura do degrau: "))
tamanho_total = float(input("Digite o valor da altura total da escada: "))
quant_degrau = 0

quant_degrau = tamanho_total // altura

if tamanho_total % altura != 0 :
    quant_degrau += 1

print(f"Você terá que subir {quant_degrau} degraus")