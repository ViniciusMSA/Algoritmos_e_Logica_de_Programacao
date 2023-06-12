#Faça uma função que retorne o valor lógico V (verdadeiro) se o número inteiro passado por parâmetro for par, e F (falso) se não. Implemente sua função em um programa completo;

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número inteiro: "))
resultado = eh_par(num)

if resultado:
    print("O número é par.")
else:
    print("O número é ímpar.")
