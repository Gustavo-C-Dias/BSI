# Faça um algoritmo que lê uma matriz M5x5. A matriz deve ser preenchida 
# através das colunas, por exemplo, se for digitado: 1,2,3,4,5,6,7,8,9,10,... 
# Após mostre a matriz resultante.

matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,]]

for coluna in range(5):
    for linha in range(5):
        matriz [linha][coluna] = int(input("Digite um valor :"))

for linha in matriz:
    for element in linha:
        print(element, end=" ")
    print()                  