#Escreva um algoritmo que calcule e mostre a area de um circulo. sabe-se que Area = pi * R²

from math import pow

pi = 3.1415
raioCirculo = float(input("Digite o valor do raio do circulo:"))
areaCirculo = pi * pow(raioCirculo, 2)
print("O valor da area do circulo é:", areaCirculo)