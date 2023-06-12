#Faça algoritmo que carregue dois vetores de dez elementos numéricos cada um e mostre um vetor resultante na intercalação desses dois vetores.

vetor1 = []
vetor2 = []
vetor_resultante = []

print("Digite os elementos do primeiro vetor:")
for i in range(10):
    elemento = int(input("Digite um elemento: "))
    vetor1.append(elemento)

print("\nDigite os elementos do segundo vetor:")
for i in range(10):
    elemento = int(input("Digite um elemento: "))
    vetor2.append(elemento)

for i in range(10):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])

print("\nVetor resultante da intercalação:")
print(vetor_resultante)
