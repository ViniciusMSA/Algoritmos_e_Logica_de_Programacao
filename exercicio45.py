#Faça um algoritmo para determinar se um determinado vetor, digitado pelo usuario, e um palindromo.

#Palindromo: Lido da direita para a esquerda, ou vice versa, representam a mesma coisa.  Ex: Ama.

vetor = input("Digite o vetor: ")
reverso = vetor[::-1]

if vetor == reverso:
    print("O vetor é um palíndromo.")
else:
    print("O vetor não é um palíndromo.")
