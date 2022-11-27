# Faça um programa que crie um arquivo texto e que salve seu nome
# neste arquivo, após sobrescreva o conteúdo deste arquivo com a
# frase “Eu amo algoritmos!”.

nome = "Gustavo Chimenes Dias"
frase = "Eu amo algoritmos!"
arquivo = open("Ex_2.txt",'w')

arquivo.write(nome)
arquivo.close

arquivo = open("Ex_2.txt",'w+')
arquivo.write(frase)
arquivo.close