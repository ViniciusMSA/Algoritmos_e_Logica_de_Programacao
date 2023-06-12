#Faça um algoritmo que leia os valores de uma matriz 3x3 de elementos reais e crie a matriz transposta da matriz fornecida. Matriz transposta: Igual a simétrica. Em matemática, é o resultado da troca de linhas por colunas em uma determinada matriz.A[i,j] = A[j,i]

matriz_original = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz_original.append(linha)

matriz_transposta = []
for i in range(3):
    linha_transposta = []
    for j in range(3):
        elemento_transposto = matriz_original[j][i]
        linha_transposta.append(elemento_transposto)
    matriz_transposta.append(linha_transposta)

print("Matriz original:")
for linha in matriz_original:
    print(linha)

print("Matriz transposta:")
for linha_transposta in matriz_transposta:
    print(linha_transposta)
