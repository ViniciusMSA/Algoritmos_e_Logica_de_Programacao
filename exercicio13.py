#Sabe-se que o quilowatt de energia custa um oitavo de salario minimo. Escreva um algoritmo que receba o
#valor do salario minimo e a quantidade de quilowatts consumidas por uma residencia. calcule e mostre:
#A) O valor, em reais, de cada quilowatt.
#B) O valor, em reais, a ser pago por essa residencia.
#C) O valor, em reais, a ser pago com desconto de 15%.

valorSalarioMinimoo = float(input("Digite em reais o valor autal do salario minimo:"))
qntdQuilowatts = float(input("Digite o valor de energia consumido pela residencia em Quilowatts:"))
valorUnQuilowatts = valorSalarioMinimoo * 0.125
print("O valor pago por cada Quilowatt consumido é de",valorUnQuilowatts)
quilowattApagar = qntdQuilowatts * valorUnQuilowatts
print("O valor a ser pago pela energia consumida pela residencia é de R$", quilowattApagar)
quilowattApagarComDesconto = quilowattApagar * (1 - 0.15)
print("O valor a ser pago pela energia consumida pela residencia com desconto de 15% é de R$", quilowattApagarComDesconto)
