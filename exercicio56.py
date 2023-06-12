#Faça um algoritmo que leia uma matriz 2x2, calcule e mostre uma matriz resultante que será a matriz digitada, multiplicada pelo maior elemento da matriz.

matriz = []

for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

maior_elemento = matriz[0][0]
for i in range(2):
    for j in range(2):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]

matriz_resultante = []
for i in range(2):
    linha_resultante = []
    for j in range(2):
        elemento_resultante = matriz[i][j] * maior_elemento
        linha_resultante.append(elemento_resultante)
    matriz_resultante.append(linha_resultante)

print("Matriz resultante:")
for i in range(2):
    for j in range(2):
        print(matriz_resultante[i][j], end=" ")
    print()
