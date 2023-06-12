#Faça um algoritmo que leia uma matriz 10x20 com números inteiros e some cada uma das linhas, armazenando o resultado das somas em um vetor. A seguir, multiplique cada elemento da matriz pela soma da linha e mostre a matriz resultante.

matriz = []
for i in range(10):
    linha = []
    for j in range(20):
        elemento = int(input(f"Digite o elemento da posição [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

soma_linhas = []
for linha in matriz:
    soma = sum(linha)
    soma_linhas.append(soma)

matriz_resultante = []
for i in range(10):
    linha_resultante = []
    for j in range(20):
        elemento = matriz[i][j] * soma_linhas[i]
        linha_resultante.append(elemento)
    matriz_resultante.append(linha_resultante)

print("Matriz Resultante:")
for linha in matriz_resultante:
    print(linha)
