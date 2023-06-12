#Faça um algoritmo que calcule a soma dos primeiros 50 numeros pares. Este algoritmo não recebe valores do teclado. Os primeiros numeros pares são 2, 4, 6...

num = 0
contador = 0
for i in range(2, 101, 2):
    num = num + i
    contador = contador + 1
print(f"A soma dos primeiros {contador} números pares é: {num}")
