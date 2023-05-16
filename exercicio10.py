#Escreva um algoritmo que receba um numero positivo e maior que zero, calcule e mostre:
#A) O numero digitado ao quadrado.
#B) O numero digitado ao cubo.
#C) A raiz quadrada do numero digitado.

from math import pow, sqrt

numero = float(input("Digite um numero positivo e maior que zero:"))
while numero <= 0:
    print("O numero digitado é invalido.")
    numero = float(input("Digite um numero positivo e maior que zero: "))
    if numero > 0:
        print("Voce digitou um numero valido:")
        break
A = pow(numero, 2)
print("O numero", numero, "elevado ao quadrado é:", A)
B = pow(numero, 3)
print("O numero", numero, "elevado ao cubo é:", B)
C = sqrt(numero)
print("A raiz quadrada do numero", numero, "é:", C)

