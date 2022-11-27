# Utilize os arquivos pares.txt e impares.txt gerados através do código-fonte,
# apresentado nos slides. Faça a leitura destes dois arquivos e crie um só arquivo
# denominado de pareseimpares.txt com base em todas as linhas dos dois arquivos
# lidos e parapreservar a ordem numérica.

impar = open ("Impares.txt","r")
par = open("Pares.txt","r")
mescla = open("Ex_4.txt","w")

conteudo_par = par.readlines()
conteudo_impar = impar.readlines()

for x in range(len(conteudo_impar)):
    mescla.write(conteudo_par[x])
    mescla.write(conteudo_impar[x])

impar.close
par.close
mescla.close