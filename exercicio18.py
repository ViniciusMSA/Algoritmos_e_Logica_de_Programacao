#Tendo como dados de entrada a altura e o sexo de uma pessoa, escreva um algoritmo que calcule seu peso
#ideal, utilizando as seguintes formulas:

#Para homens: (72.7 * h) - 58;
#Para mulheres: (62.1 * h) - 44.7

sexo = input("Digite o seu sexo: M para homem ou F para mulher:")
altura = float(input("Digite a sua altura:"))
if sexo == "M":
    peso = (72.7 * altura) - 58
    print("O seu peso ideal é:", peso)
elif sexo == "F":
    peso = (62.1 * altura) - 44.7
    print("O seu pedo ideal é:", peso)
else:
    print("Digite um valor valido: M para homem e F para mulher (em maiusculo).")
