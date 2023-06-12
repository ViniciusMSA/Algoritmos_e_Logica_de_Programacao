#Faça um algoritmo que:
# -Leia um numero indeterminado de valores que representam, cada um, a idade de um individuo.
# -Para finalizar, o usuario deverá digitar 0, que não entrará nos calculos.
# -Calcule e mostre a idade média e o numero total de pessoas deste grupo de individuos.

contadorPessoas = 0
idadeTotal = 0

while True:
    idade = int(input(f"Pessoa Nª{contadorPessoas+1}: Digite a sua idade: "))
    contadorPessoas = contadorPessoas + 1
    idadeTotal = idadeTotal + idade
    media = idadeTotal / contadorPessoas
    if idade == 0:
        print(f"A média de idade das {contadorPessoas-1} pessoas é {media} anos.")
        break
    else:
        continue
