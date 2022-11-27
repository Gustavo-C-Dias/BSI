# Faça um algoritmo que percorre uma lista com o seguinte formato: 
#   [
#       ['Brasil', 'Italia', [10, 9]], 
#       ['Brasil', 'Espanha', [5, 7]], 
#       ['Italia', 'Espanha', [7,8]]
#   ]. 
# Essa lista indica o número de faltas que cada time fez em cada jogo.
# Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas
# e a Itália fez 9. O programa deve imprimir na tela: 
#   o total de faltas do campeonato;
#   o time que fez mais faltas;
#   o time que fez menos faltas;

matriz = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 9]], ['Italia', 'Espanha', [7,8]]]
total_faltas = 0
faltas = []
times = []
index_mais_falta = 0
index_menos_falta = 0
valor_mais_falta = 0
valor_menos_falta = 0

for x in matriz :
    for element in x :
        if list == type(element):
            for y in element:
                total_faltas += y

valor_menos_falta = matriz[0][2][0]

for x in range(len(matriz)) :
    for y in range(len(matriz[x])-1) :
        if matriz[x][y] not in times:
            times.append(matriz[x][y])
            faltas.append(matriz[x][2][y])
        else:
            for d in range(len(times)):
                if matriz[x][y] == times[d]:
                    faltas[d] += matriz[x][2][y]

    if faltas[x] <= valor_menos_falta:
        index_menos_falta = x
        valor_menos_falta = faltas[x]
    if faltas[x] >= valor_mais_falta:
        index_mais_falta = x
        valor_mais_falta = faltas[x]

print(total_faltas)
print(f"O time {times[index_menos_falta]} foi quem cometeu menos falta com {faltas[index_menos_falta]}")
print(f"O time {times[index_mais_falta]} foi quem cometeu mais falta com {faltas[index_mais_falta]}")                       