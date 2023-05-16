#Escreva um programa que calcule a distancia entre dois pontos

from math import pow, sqrt
#pow(X, Y): Retorna X elevado a potencia de Y. Ex: pow(5, 2) -> 5² -> 25
#sqrt(X): Retorna a raiz quadrada de X

x1 = float(input("Digite o valor de x1:"))
y1 = float(input("Digite o valor de y2:"))
x2 = float(input("Digite o valor de x2:"))
y2 = float(input("Digite o valor de y2:"))
dx = x2 - x1
dy = y2 - y1
d = sqrt(pow(dx, 2) + pow(dy, 2))
print("A Distancia é: D = ", d)
