#Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre a sua idade e, também
#verifique e mostre se ela ja tem idade para votar (16 anos ou mais) e para conseguir a carteira de
#habilitação (18 anos ou mais)

idade = int(input("Digite a sua idade:"))
if idade >= 18:
    print("Parabens, voce ja pode votar e tirar carteira de habilitação.")
elif idade < 18 and idade >= 16:
    print("Parabens, voce ja pode votar. Mas, infelizmente, ainad nao pode tirar a carteira de habilitação.")
else:
    print("Infelizmente voce nao tem 16 anos. Não pode votar.")