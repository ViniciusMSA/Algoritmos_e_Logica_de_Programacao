#Faça um programa que receba um numero inteiro maior que 1. Ele deve verificar se o numero fornecido é primo ou não, e mostrar a mensagem correspondente.
#Lembre-se: Um numero primos é divisivel por 1 ou por ele mesmo.

num = int(input("Digite um número inteiro maior que 1: "))

if num > 1:
    eh_primo = True

    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print("O número digitado é primo.")
    else:
        print("O número digitado não é primo.")
else:
    print("O número deve ser maior que 1.")
