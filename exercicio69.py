#Construa uma função que retorne o MDC de dois números inteiros passados por parâmetro.

def calcular_mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

mdc = calcular_mdc(num1, num2)
print("O MDC entre", num1, "e", num2, "é", mdc)
