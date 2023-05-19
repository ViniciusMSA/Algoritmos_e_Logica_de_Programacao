#Escreva um programa que receba um numero inteiro e verifique se esse numero é par ou impar

num = float(input("Digite um numero:"))
imparOuPar = num % 2
if imparOuPar == 0:
    print("O numero digitado é par.")
else:
    print("O numero digitado é impar.")
    