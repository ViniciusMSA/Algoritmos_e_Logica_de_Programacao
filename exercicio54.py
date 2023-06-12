#Faça um algoritmo que lê 10 números inteiros e os armazena em um vetor A. Depois de armazenado, o algoritmo fará a ordenação desses números (em ordem crescente de valores) e os colocará no vetor B Ao final o algoritmo deve mostrar os dois vetores: A e B.

A = []
B = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    A.append(num)

B = sorted(A)

print("Vetor A:", A)
print("Vetor B:", B)
