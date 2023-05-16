#Escreva um algoritmo que recebe o valor de um deposito e o valor da taxa de juros, calcule e mostre o 
#valor do rendimento e o valor total depois do rendimento.

valorDeposito = float(input("Digite o valor do deposito:"))
x = float(input("Digite o valor da taxa de juros:"))
taxaJuros = x / 100
rendimento = valorDeposito * taxaJuros
valorFinal = valorDeposito + rendimento
print("O valor do deposito mais rendimento é de: R$", valorFinal)