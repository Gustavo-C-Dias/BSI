#O TSE disponibiliza os dados das eleições em seu portal de Dados Abertos. O arquivo “eleicoes.csv”
2# foi obtido do portal, e traz os dados referentes aos boletins de urna do segundo turno das eleições
# de 2022, para o estado de SC.Os dados estão no formato CSV (Valores Separados por Vírgula).

#Faça um programa que manipule os dados do arquivo, e:
    # 1 - Crie um arquivo contendo apenas os códigos e nomes dos municípios do estado;

    # Crie um procedimento que receba o código de um município e crie um arquivo contendo uma lista
    # das seções de votação, a quantidade de votantes aptos, a quantidade de votantes que compareceram,
    # e a quantidade de abstenções;

    #Crie um procedimento que receba o código de um município e crie um arquivo contendo a quantidade de
    # votantes aptos, a quantidade de votantes que compareceram, e a quantidade de abstenções no município;

def municipios (matriz):
    municipios = open ("municipios.txt","w")
    municipios_ler = open("municipios.txt","r")

    for x in range(1,len(matriz)): 
        municipios.write(f'{matriz[x][11]}')
        municipios.write(f'{matriz[x][12]}\n')

    municipios.close
    municipios_ler.close

matriz = []
arquivo = open("eleicoes.csv",'r')
conteudo = arquivo.readlines()
for x in range(len(conteudo)):
    linha = conteudo[x].split(';')
    matriz.append(linha)

municipios(matriz)

arquivo.close