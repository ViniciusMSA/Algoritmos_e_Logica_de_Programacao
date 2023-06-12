#Faça um algoritmo que carregue um vetor de 10 elementos numéricos inteiros. Após a finalização da entrada, o algoritmo deve escrever o mesmo vetor, na ordem inversa de entrada.

vetor = []

for i in range(10):
    if i == 0:
        elemento = int(input("Digite um elemento: "))
        vetor.append(elemento)
    else:
        elemento = int(input("Digite outro elemento: "))
        vetor.append(elemento)

vetorInverso = vetor[::-1]
print("Vetor na ordem inversa:")
print(vetorInverso)
