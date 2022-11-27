# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no
# seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa
# saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado.
# Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
# "usuarios.txt":

    # alexandre      456123789
    # anderson       1245698456
    # antonio        123456456
    # carlos         91257581
    # cesar          987458
    # rosemary       789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar
# um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:

    # ACME Inc.               Uso do espaço em disco pelos usuários
    # ----------------------------                                                                      --------------------------------------------
    # Nr.  Usuário        Espaço utilizado     % do uso

    # 1    alexandre        434,99 MB            16,85%
    # 2    anderson         1187,99 MB           46,02%
    # 3    antonio          117,73 MB            4,56%
    # 4    carlos           87,03 MB             3,37%
    # 5    cesar            0,94 MB              0,04%
    # 6    rosemary         752,88 MB            29,16%

    # Espaço total ocupado: 2581,57 MB
    # Espaço médio ocupado: 430,26 MB

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam
# necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco,
# de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo
# programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função,
# que será chamada pelo programa principal.


def conversao_mb(valor):
    for x in range(len(matriz)):
        valor[x][2] = round((valor[x][2]/1048576),2)

def porcentual(valor):
    total_ocupado = 0
    for x in range(len(matriz)):
        total_ocupado += valor[x][2]

    for x in range(len(matriz)):
        valor[x].append(round((100*valor[x][2])/total_ocupado,2)) 
        #round(valor, casas decimais) arredondamento de um valor.
    
    return total_ocupado

arquivo = open ("usuario.txt","r")
matriz = []
id = 1

conteudo = arquivo.readlines()

for x in range(len(conteudo)):
    aux = []
    aux.append(id)
    aux.append(conteudo[x][:15].replace(" ",""))
    #replace(" ","") tirar espaços em branco, troca por nada.
    aux.append(int(conteudo[x][15:len(conteudo[x])]))
    matriz.append(aux)
    id += 1

conversao_mb(matriz)
total_ocupado = porcentual(matriz)
arquivo.close

arquivo = open("Relatorio.txt","w+")
arquivo.write("ACME Inc.           Uso do espaco em disco pelos usuarios")
arquivo.write("\n"+"-"*57+"\n")
arquivo.write(" Nr.  Usuario             Espaco utilizado     % do uso\n")

for x in matriz:
    cont = 0
    for y in x:
        if (cont == 1):
            arquivo.write(f'  {y}'.title())
            #title() deixar a primeira letra maiúscula
            tamanho = len(f'{y}')
            escrever = " " * (19-tamanho)
            arquivo.write(escrever)
        else:
            arquivo.write(f' {y}')
            tamanho = len(f'{y}')
            escrever = " " * (3-tamanho)
            arquivo.write(escrever)
            cont = 1
    arquivo.write("\n")
arquivo.write(f"\n Espaço total ocupado: {total_ocupado} MB")
medio_ocupado = round(total_ocupado / len(matriz),2)
arquivo.write(f"\n Espaço médio ocupado: {medio_ocupado} MB")


arquivo.close