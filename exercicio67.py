#Faça uma função que retorne o valor lógico V (verdadeiro) se o número inteiro passado por parâmetro for primo, e F (falso) se não. Implemente sua função em um programa completo.

def eh_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

num = int(input("Digite um número inteiro: "))
resultado = eh_primo(num)

if resultado:
    print("O número é primo.")
else:
    print("O número não é primo.")
