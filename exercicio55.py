#Faça um algoritmo que leia uma matriz 2x2 e imprima os seus elementos na ordem:
#1,1 =
1#,2 =
#2,1 =
#2,2 =
#Obs: linha, coluna

matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

for i in range(2):
    for j in range(2):
        print(f"{matriz[i][j]}")

