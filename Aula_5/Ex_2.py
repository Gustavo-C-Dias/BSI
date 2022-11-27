resultado = (1,2,3,4,5)
aposta = list()
i = 0

for x in range(10):
    aposta.append(int(input(f"Digite o {x} valor da sequencia de aposta : ")))

for tuple_element in resultado :
    for list_element in aposta :
        if list_element == tuple_element :
            i += 1

print(i)


# Professora

R = set()
S = set()

for i in range(5):
    R.add(int(input(f"Digite o {i} numero da 1º lista : ")))

print("\n------\n")

for i in range(10):
    S.add(int(input(f"Digite o {i} numero da 2º lista : ")))

X = R & S
print(len(X))