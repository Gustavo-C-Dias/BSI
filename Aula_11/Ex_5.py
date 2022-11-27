par = open("Pares.txt","r+")
par_inversa = []

conteudo = par.readlines()
for x in range((len(conteudo)-1), -1, -1):
    par_inversa.append(conteudo[x])
par.close

par_escrita = open("Pares.txt","w")
for x in range(len(par_inversa)):
    par_escrita.write(par_inversa[x])
par_escrita.close