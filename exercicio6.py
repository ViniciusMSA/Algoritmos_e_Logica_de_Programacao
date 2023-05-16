#Escreva um algoritmo que receba o salario de um funcionario e o percentual de aumento, calcule e mostre
#o valor do aumento e o novo salario.

salarioAtual = float(input("Digite o seu salario atual:"))
X = float(input("Digite o valor do reajuste salarial:")) #Recebe valor reajuste
reajuste = X / 100 #Converte valor reajuste p/ decimal
novoSalario = salarioAtual * (1 + reajuste)
print("O valor inicial do salario é de:", salarioAtual)
print("O valor do reajuste é de",reajuste)
print("O valor do salario apos o reajuste é de: R$",novoSalario)