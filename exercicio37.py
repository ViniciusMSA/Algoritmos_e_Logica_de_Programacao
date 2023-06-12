#Exercicio repetido.
#O enunciado é exatamente o mesmo do exercicio 29.

#Faça um programa que receba um numero inteiro X. Calcule e mostre o fatorial desse numero (X!).

num = int(input("Digite um numero inteiro: "))
fatorial = 1

if num == 0 or num == 1:
    print(f"O fatorial de {num} é 1.")
else:
    for i in range (1, num+1):
        fatorial = fatorial * i
    print(f"O fatorial de {num} é {fatorial}")