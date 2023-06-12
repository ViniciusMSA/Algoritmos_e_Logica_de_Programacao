#Elabore um algoritmo que simule uma contagem regressiva de 10 minutos, ou seja, mostre 10:00 e entao,9:59, 9:58,..., 9:00; 8:59, 8:58, até 0:00

import time

minutos = 10

for minuto in range(minutos, -1, -1):
    for segundo in range(59, -1, -1):
        print(f"{minuto:02d}:{segundo:02d}")
        time.sleep(1)
