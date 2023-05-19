#Escreva um algoritmo que receba a idade de um nadador e mostre a sua categoria usando as regras a seguir:
#Categoria..........#Idade
#Infantil...........#5 a 7
#Juvenil............#8 a 10
#Adolescente........#11 a 15
#Adulto.............#16 a 30
#Senior.............#acima de 30

idade = int(input("Digite a sua idade:"))
if idade < 5:
    print("Voce nao tem idade o suficiente.")
elif idade >= 5 and idade <= 7:
    print("A sua categoria é: Infantil")
elif idade > 7 and idade <= 10:
    print("A sua categoria é: Juvenil")
elif idade > 10 and idade <= 15:
    print("A sua categoria é: Adolescente")
elif idade > 15 and idade <= 30:
    print("A sua categoria é: Adulto")
else:
    print("A sua categoria é: Senior")
