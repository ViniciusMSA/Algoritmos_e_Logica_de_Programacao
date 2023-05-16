#Cada degrau de uma escada tem xCm de altura. Faça um algoritmo que receba  a altura de cada  degrau em
#cm e a altura que o usuario deseja alcançar subindo a escada (em metros). Faça as conversões, calcule
#e mostre quantos degruas o usuario devera subir para atingir seu objetivo.

alturaDegrausEmCm = int(input("Digite a altura de cada degrau em centímetros: "))
alturaDesejadaEmMetros = float(input("Digite a altura que você deseja alcançar subindo a escada em metros: "))

alturaDegrauEmMetros = alturaDegrausEmCm / 100
alturaDesejadaEmCm = alturaDesejadaEmMetros * 100

numeroDegraus = round(alturaDesejadaEmCm / alturaDegrauEmMetros)

print("Você precisará subir", numeroDegraus, "degraus para alcançar a altura desejada.")
