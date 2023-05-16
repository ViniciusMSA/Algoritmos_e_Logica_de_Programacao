#Escreva um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual e mostra:
#A: A idade dessa pessoas em anos
#B: A idaide dessa pessoa em meses
#C: A idade dessa pessoa em dias
#D: A idade dessa pessoa em semanas

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

