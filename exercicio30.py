#Faça um programa que calcule os 10 primeiros numeros da sequencia de fibonacci

n = 10
fibonacci = [0, 1]

for i in range(2, n):
    termo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(termo)

for termo in fibonacci:
    print(termo)
