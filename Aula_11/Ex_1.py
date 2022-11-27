# Faça um programa que crie um arquivo texto e que salve seu nome
# neste arquivo (o nome deve ser informado via terminal).

nome = input("Digite o seu nome: ")

arquivo = open('Ex_1.txt','w')
arquivo.write(nome)
arquivo.close