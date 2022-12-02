# Instituto Federal Catarinense - Campus Camboriú
# Aluno: Gustavo Chimenes Dias
# Disciplina: Algoritmos e Programação de Computadores II - Lidiane

def cadastrar_equipe():
    print("-" * 50 + "\n - Cadastrar Equipes")
    equipes = []

    while True:
        controle = int(input("\n   📝 1 - Nova equipe\n   🔑 2 - Salvar\n\n Digite um valor: "))

        match controle:
            case 1:
                pais = input("Digite o nome do país:").upper()
                if not(verificar_cadastro_arquivo(pais) or verificar_cadastro_lista(pais,equipes)): 
                    aux = []
                    aux.append(pais)
                    aux.append(input(f"Digite a sigla do {pais}: ").upper())
                    aux.append(input(f"Grupo que o {pais} está: ").upper())
                    equipes.append(aux)
                else:
                    print("❗ Já cadastrado")
            case 2:
                gravar(equipes, "equipes")
                break
            case _:
                print("\n ❌ Digite um valor válido!")
            
     
def cadastrar_jogo():
    print("-" * 50 + "\n - Cadastrar Jogos\n")  
    jogos = []
    
    while True:
        aux = []
        equipe_B = []
        equipe_A = []
        controle = int(input("\n   📝 1 - Novo jogo\n   🔑 2 - Salvar\n\n Digite um valor: "))

        match controle:
            case 1:
                equipe_A.append(input("Digite o nome da primeira equipe: ").upper())
                if not(verificar_cadastro_arquivo(equipe_A[0])):
                    cadastrar_equipe()
                equipe_B.append(input("Digite o nome da segunda equipe: ").upper())
                if not(verificar_cadastro_arquivo(equipe_B[0])):
                    cadastrar_equipe()

                print(f"\nInformações sobre o {equipe_A[0]} no jogo: ")
                equipe_A.append(input("Quantidade de gols : "))
                equipe_A.append(input("Quantidade de faltas: "))
                print(f"\nInformações sobre o {equipe_B[0]} no jogo: ")
                equipe_B.append(input("Quantidade de gols: "))
                equipe_B.append(input("Quantidade de faltas: "))

                for elemento in equipe_A:
                    aux.append(elemento)
                aux.append("#")
                for elemento in equipe_B:
                    aux.append(elemento)
                jogos.append(aux)
            case 2:
                gravar(jogos, "jogos")
                break
            case _:
                print("\n ❌ Digite um valor válido!")


def total_jogos():
    print("-" * 50 + "\n - Total de jogos\n")
    try:
        arquivo_jogos = open("jogos.txt","r")
        conteudo = tratar_conteudo(arquivo_jogos.readlines())
        arquivo_jogos.close
        print(f"{len(conteudo)} é a quantidade total de jogos cadastrado")
    except:
        print("🚨 Cadastre um jogo primeiro 🚨")


def total_equipes():
    print("-" * 50 + "\n - Total de equipes\n")
    try:
        arquivo_equipes = open("equipes.txt","r")
        conteudo = tratar_conteudo(arquivo_equipes.readlines())
        arquivo_equipes.close
        print(f"{len(conteudo)} é a quantidade total de equipes cadastradas")
    except:
        print("🚨 Cadastre uma equipe primeiro 🚨")
    

def listar_jogos():
    print("-" * 50 + "\n - Listagem dos jogos\n")
    try:
        arquivo_jogos = open("jogos.txt","r")
        conteudo = tratar_conteudo(arquivo_jogos.readlines())
        arquivo_jogos.close
        print("Time\tGol\tFalta\tVs\tTime\tGol\tFalta\n")
        for linha in conteudo:
            for elemento in linha:
                print(elemento, end="\t") 
            print("")
    except:
        print("🚨 Cadastre um jogo primeiro 🚨")


def pesquisar ():
    print("-" * 50 + "\n - Pesquisa\n")
    try:
        arquivo_equipes = open("equipes.txt","r")
        conteudo = tratar_conteudo(arquivo_equipes.readlines())
        arquivo_equipes.close

        equipe = input("Digite a equipe que deseja buscar: ").upper()
        for linha in range(len(conteudo)):
            if equipe == conteudo[linha][0]:
                print(f"Pais: {conteudo[linha][0]}")
                print(f"Sigla: {conteudo[linha][1]}")
                print(f"Grupo: {conteudo[linha][2]}")

        arquivo_jogos = open("jogos.txt","r")
        conteudo = tratar_conteudo(arquivo_jogos.readlines())
        arquivo_jogos.close

        jogou = False
        faltas = 0
        gols = 0
        for linha in range(len(conteudo)):
            if equipe == conteudo[linha][0]:
                jogou = True
                print(conteudo[linha])
                gols += int(conteudo[linha][1])
                faltas += int(conteudo[linha][2])

            if equipe == conteudo[linha][4]:
                jogou = True
                print(conteudo[linha])
                gols += int(conteudo[linha][5])
                faltas += int(conteudo[linha][6])

        if jogou:
            print(f"{gols} gols totais")
            print(f"{faltas} faltas totais")
        else:
            print(f"O pais {equipe} não tem jogos")                 
    except:
        print("🚨 Cadastre uma equipe primeiro 🚨")
    
 
def tratar_conteudo(conteudo):
    aux = []
    for elemento in conteudo:
        aux.append(elemento.split(";"))
    return aux

def verificar_cadastro_arquivo(pais):
    try:
        arquivo_equipe = open ("equipes.txt","r+")
        conteudo = tratar_conteudo(arquivo_equipe.readlines())
    except:
        arquivo_equipe = open("equipes.txt","w+")
        conteudo = tratar_conteudo(arquivo_equipe.readlines())
    arquivo_equipe.close
    for linha in range(len(conteudo)):
        if pais.upper() == conteudo[linha][0]:
            return True
    return False

def verificar_cadastro_lista(pais, equipe):
    for linha in range(len(equipe)):
        if pais.upper() == equipe[linha][0]:
            return True
    return False

def gravar(conteudo, tipo):
    match tipo:
        case "equipes":
            arquivo = open ("equipes.txt","a+")
        case "jogos":
            arquivo = open ("jogos.txt","a+")
    for linha in conteudo:
        for elemento in linha:
            arquivo.write(f"{elemento};")
        arquivo.write("\n")
    arquivo.close
              
while True :
    controle = int(input("\nO programa pode executar as funções: \n\n"+
    "   📝 1 - Cadastrar nova equipe\n"+
    "   📝 2 - Cadastrar novo jogo \n"+
    "   📈 3 - Total de equipes armazenadas\n"+
    "   📊 4 - Total de jogos armazenados\n"+
    "   ⚽ 5 - Listar todos os jogos\n"+
    "   🔎 6 - Pesquisar\n"+
    "   🔑 7 - Sair\n"+
    "   \nDigite o valor de uma das funções:"))

    match controle:
        case 1:
            cadastrar_equipe()
        case 2:
            cadastrar_jogo()
        case 3:
            total_equipes()
        case 4:
            total_jogos()
        case 5:
            listar_jogos()
        case 6:
            pesquisar()
        case 7:
            break
        case _:
            print("\n ❌ Digite um valor válido!")