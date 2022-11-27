# Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros. 
# Gere um vetor X que possua os elementos comuns a R e a S. Considere que
# no mesmo vetor não haverá números repetidos.

R = list()
S = list()
X = list()
cont = 0

for x in range (5):
    R.append(int(input(f"{x+1} numero para 1º lista :")))

print("------------")

for x in range (10):
    S.append(int(input(f"{x+1} numero para 2º lista :")))

for y in S:
    for x in R:
       if y == x :
           X.append(y)

for index1, valor1 in enumerate(X):
    for index2, valor2 in enumerate(X):
        if valor2 == valor1 :
            cont += 1
        if cont > 1 :
            del X[index2]
    cont = 0

print(X)