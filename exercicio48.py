#Faça um algoritmo que carregue um vetor de 10 elementos numéricos inteiros. Após a finalização da entrada, o algoritmo deve escrever o maior valor e sua posição.

vetor = []

for i in range(1, 11):
    elemento = int(input("Digite um elemento: "))
    vetor.append(elemento)

maiorValor = vetor[0]
posicao_maior = 0

for i in range(1, len(vetor)):
    if vetor[i] > maiorValor:
        maiorValor = vetor[i]
        posicao_maior = i

print(f"O maior valor é {maiorValor} e está na posição {posicao_maior}.")
