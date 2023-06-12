#Construa um algoritmo que calcule a média aritmética de um conjunto de numeros pares que forem fornecidos pelo usuario. O valor de finalização sera a entrada do numero 0. Observe que nada impede que o usuário forneça quantos numeros impares quiser, com a ressalva de que eles não poderão ser acumulados.

conjunto = int(input("Digite a quantidade de numeros que serão digitados: "))
valorTotal = 0

for i in range(1, conjunto+1):

    if i == 1:
        num = int(input("Digite um numero: "))
    else:
        num = int(input("Digite outro numero: "))

    if num == 0:
        print("Voce digitou o numero zero, encerrando o algoritmo...")
        break

    if num % 2 == 0:
        print("O numero digitado é par!")
        valorTotal = valorTotal + num
        media = valorTotal / i
        if i != conjunto:
            print(f"A média dos valores digitados até o momento é: {media}")
        else:
            print(f"A média final dos valores digitados é: {media}")
    else:
        print("O numero digitado é impar! Digite um numero par para calcular a média.")
print("Fim do algoritmo!")