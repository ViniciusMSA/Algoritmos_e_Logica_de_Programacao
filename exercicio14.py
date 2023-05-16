#Escreva um algoritmo que receba uma hora formatada por hora e minutos (um numero real), calcule e mostre
#a hora digitada apenas em minutos. Lembre-se de que:
    #Para quatro e meia deve-se digitar: 4,30
    #Os minutos vão de 0 a 60.

horaDigitada = float(input("Digite a hora no formato decimal (exemplo 04:30: 4.30): "))

horas = int(horaDigitada)
minutosDecimal = horaDigitada - horas
minutos = int(horas * 60 + minutosDecimal * 100)

print("A hora digitada em minutos é:", minutos, "minutos.")
