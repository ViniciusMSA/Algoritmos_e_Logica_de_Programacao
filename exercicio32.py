#Faça um algoritmo que leia dois valores B e N inteiros e positivos, calcule e mostre o valor E, conforme a fórmula a seguir:

# E = [B**1] + [B**2] +[B**3] + ... + [B**N]

B = int(input("Digite um numero inteiro e positivo: "))
N = int(input("Digite um numero inteiro e positivo: "))
E = 0

while B <= 0 or N <= 0:
    print("Voce digitou um valor invalido.")
    B = int(input("Digite um numero inteiro e positivo: "))
    N = int(input("Digite um numerointeiro e positivo: "))
for i in range (1, N+1):
    potenciacao = B**i
    E += potenciacao
print(f"Dados os valores de B e N, o valor de E é {E}")