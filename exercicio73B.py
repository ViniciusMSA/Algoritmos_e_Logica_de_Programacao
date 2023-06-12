#ARQUIVO: funcoes.py: Importe o pacote “Random” e prepare uma função função que irá retornar aleatoriamente um valor de um dos lados de um dado (valores variando de 1 a 6). ARQUIVO:jogo.py Importe o arquivo funções.py Implemente um programa de jogo de dados entre você e o computador, usando essa função.

import exercicio73

def jogo_de_dados():
    jogador = exercicio73.rolar_dado()
    print("Jogador: ", jogador)
    
    computador = exercicio73.rolar_dado()
    print("Computador: ", computador)
    
    if jogador > computador:
        print("Você venceu!")
    elif jogador < computador:
        print("O computador venceu!")
    else:
        print("Empate!")

jogo_de_dados()
