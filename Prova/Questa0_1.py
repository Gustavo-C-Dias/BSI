A = []
A_invert = []
B = []
B_invert = []
N = 3

for x in range(N):
    A.append(int(input(f"Digite o valor {x} para estrutura A: ")))

for x in range(N):
    B.append(int(input(f"Digite o valor {x} para estrutura B: ")))

index = len(A)-1
for x in range(N):
    A_invert.append(A[index])
    B_invert.append(B[index])
    index -= 1

print(f"\nA lista A invertida fica: {A_invert}")
print(f"A lista B invertida fica: {B_invert}")