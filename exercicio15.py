#Escreva um algoritmo que leia dois numeros e escreva o menor deles

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
if num1 > num2:
    print("O maior numero digitado é o numero", num1)
else:
    print("O maior numero digitado é o numero", num2)