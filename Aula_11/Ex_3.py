# Escreva um programa que receba do usuário 5 números inteiros e o nome
# do arquivo no qual eles devem ser armazenados. Em seguida, ler do
# arquivo os valores armazenados copiando-os para uma lista de inteiros
# e os imprimindo na tela.

nome_arquivo = input("Digite o nome do arquivo: ")
arquivo = open (f"{nome_arquivo}.txt", 'w')
quantidade = 5
lista = []

for x in range(quantidade):
    valor = input("Digite um valor: ")
    arquivo.write(f"{valor}\n")
arquivo.close

arquivo = open (f"{nome_arquivo}.txt", 'r')
for x in arquivo.readlines():
    lista.append(int(x))
arquivo.close

for x in range(len(lista)):
    print(lista[x])



# Usando metodo split()

#arquivo = open (f"{nome_arquivo}.txt", 'r')
#for x in arquivo.readlines():
#    aux = x.split()
#    lista.append(aux)
#arquivo.close
#for x in range(len(lista)):
#    print(lista[x])