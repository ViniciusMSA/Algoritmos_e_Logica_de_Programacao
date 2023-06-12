#Faça um algoritmo que calcule a area de um triangulo. Este algoritmo não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a zero.

# Area = B * H
#        -----
#          2

base = int(input("Digite o valor da base do triangulo: "))
altura = int(input("Digite o valor da altura do triangulo: "))

while base <= 0 or altura <= 0:
    print("Voce digitou um numero inválido. Digite um valor maior do que zero.")
    base = int(input("Digite o valor da base do triangulo: "))
    altura = int(input("Digite o valor da altura do triangulo: "))
area = (base * altura) / 2
print(f"A area do triangulo é {area}")
