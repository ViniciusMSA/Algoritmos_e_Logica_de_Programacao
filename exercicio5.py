#Escreva um algoritmo que receba o salario de um funcionario, calcule e mostre um novo salario,
#sabendo-se que este sofreu um reajuste de 25%.

salarioAtual = float(input("Digite o seu salario:"))
reajuste = 0.25
novoSalario = salarioAtual * (1 + 0.25)
print("O seu salario reajustado em 25% é:", novoSalario)
