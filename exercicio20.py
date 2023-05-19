#Escreva um algoritmo que receba dois numeros e execute as operações listadas a seguir de acordo com a
#escolha do usuario:

#1: Média entre os numeros digitados
#2: diferença do maior pelo menos
#3: Produto entre os numeros digitados
#4: Divisão do primeiro pelo segundo

num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
operacao = int(input(
"""Digite a operação desejada: 
    1- Média entre os numeros digitados
    2- Diferença do maior pelo menor
    3- Produto entre os numeros digitados
    4- Divisão do primeiro pelo segundo 
Operacao: """))
if operacao == 1:
    media = (num1 + num2) / 2
    print("Voce escolheu a operação numero 1. A media dos dois numeros é", media)
elif operacao == 2:
    if num1 > num2:
        diferenca = num1 - num2
    elif num1 < num2:
        diferenca = num2 - num1
    else:
        diferenca = 0
    print("Voce escolheu a operação numero 2. A diferença dos dois numeros é", diferenca)
elif operacao == 3:
    produto = num1 * num2
    print("Voce escolheu a operação numero 3. O produto dos dois numeros é", produto)
else:
    if num1 > num2:
        divisao = num1 / num2
    else:
        divisao = num2 / num1
    print("Voce escolheu a operação numero 4. A divisão dos dois numeros é", divisao)