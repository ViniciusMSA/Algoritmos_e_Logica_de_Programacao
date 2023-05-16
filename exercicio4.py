#Escreva um algoritmo que receba a data de nascimento de uma pessoa e a data atual e mostre a sua idade
#em anos, meses, semanas e dias.

anoNascimento = int(input("Digite o ano que voce nasceu:"))
anoAtual = int(input("Digite o ano atual:"))
A = anoAtual - anoNascimento
print("A sua idade em anos é:",A)
B = A * 12
print("A sua idade em meses é:", B)
C = B * 365
print("A sua idade em dias é:", C)
D = float(B * 4.5)
print("A sua idade em semanas é:", D)

#Observação: Mesmo enunciado do exercicio 3.