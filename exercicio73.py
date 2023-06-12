#ARQUIVO: funcoes.py: Importe o pacote “Random” e prepare uma função função que irá retornar aleatoriamente um valor de um dos lados de um dado (valores variando de 1 a 6). ARQUIVO:jogo.py Importe o arquivo funções.py Implemente um programa de jogo de dados entre você e o computador, usando essa função.

import random

def rolar_dado():
    return random.randint(1, 6)
