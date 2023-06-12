#Crie uma função que receba como parâmetro 3 números interios (representando horas, minutos e segundos). A função deve converter em segundos. Por exemplo: 2 h, 40 min e 10 segundos correspondem a 9.610 segundos.

def converter_para_segundos(horas, minutos, segundos):
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

horas = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

total_segundos = converter_para_segundos(horas, minutos, segundos)
print("O total de segundos é:", total_segundos)
