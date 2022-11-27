with open ("Impares.txt", "w") as impares:
    with open ("Pares.txt", "w") as pares:
        for n in range(0, 19):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")