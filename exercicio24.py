#Escreva um algoritmo que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a formula a seguir.

#E = [2**1] + [2**2] + [2**3] + ... + [2**N]
#      2         4       8

N = int(input("Digite um valor N inteiro e positivo: "))

E = 0
for i in range(1, N+1):
    potenciacao = (2**i)
    E = E + potenciacao
print(f"O valor de E é: {E}")
