#Faça um Algoritmo que simule 6000 jogadas de um dado de 6 faces. Para simular o resultado utilize a função randint. Ao final, mostre a frequência de sorteio de cada uma das faces.

import random

frequencia = [0, 0, 0, 0, 0, 0]

for _ in range(6000):
    resultado = random.randint(1, 6)
    frequencia[resultado - 1] += 1

for face in range(6):
    print(f"Frequência da face {face+1}: {frequencia[face]}")