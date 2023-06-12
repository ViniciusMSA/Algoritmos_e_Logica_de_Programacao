#Faça um algoritmo que simule a jogada de dois dados de 6 faces. O programa deve usar randint para rolar o primeiro dado e deve usar randint novamente para rolar o segundo dado. A soma das duas faces deve ser calculada. Assim: a soma variará de 2 a 12 O programa deve rolar 30000 vezes e mostrar a frequência com que a soma (de 2 a 12) aparecem. Verifique se o valor 7 corresponde a 1/6 das jogadas!

import random

frequencia = [0] * 11

for _ in range(30000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    frequencia[soma - 2] += 1

for soma in range(2, 13):
    indice = soma - 2
    porcentagem = (frequencia[indice] / 30000) * 100
    print(f"Frequência da soma {soma}: {frequencia[indice]} ({porcentagem:.2f}%)")

frequencia_7 = frequencia[5]
porcentagem_7 = (frequencia_7 / 30000) * 100
print(f"\nFrequência da soma 7: {frequencia_7} ({porcentagem_7:.2f}%)")

