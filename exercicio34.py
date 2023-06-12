#Faça um algoritmo que leia um numero não determinado de pares de valores [M, N], todos inteiros e positivos, um par de cada vez e que calcule e mostre a soma de todos os numeros inteiros entre M e N (inclusive). Na digitação dos pares M, N deve-se validar que M é maior que N.

while True:
    soma = 0

    print("Inicio do algoritmo.")
    print("Digite dois valores para M e N respectivamente, sendo M maior do que N.")

    M = int(input("Digite um numero inteiro e positivo para M: "))
    while M <=0:
        print("Voce digitou um valor invalido.")
        M = int(input("Digite um numero inteiro e positivo para M: "))

    N = int(input("Digite um numero inteiro e positivo para N: "))
    while N <= 0:
        print("Voce digitou um valor invalido.")
        N = int(input("Digite um numero inteiro e positivo para N: "))
    while N >= M:
        print("O valor de M deve ser maior do que o valor de N. Por favor, digite outro numero.")
        N = int(input("Digite um numero menor do que M: "))

    for i in range(N+1, M):
        soma = soma + i
        
    print(f"A soma de valores entre M e N é: {soma}")
    fimAlgoritmo = input("Para encerrar o algoritmo, digite ENCERRAR.")
    if fimAlgoritmo == "ENCERRAR":
        print("Algoritmo encerrado.")
        break
    else:
        continue