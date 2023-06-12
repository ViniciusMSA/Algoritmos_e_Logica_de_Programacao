#Faça algoritmo que carregue duas listas de dez elementos numéricos inteiros cada um. A partir dessas duas listas, crie um conjunto da união entre essas duas listas.

lista1 = []
lista2 = []

print("Digite os elementos da primeira lista:")
for i in range(10):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    lista1.append(elemento)

print("Digite os elementos da segunda lista:")
for i in range(10):
    elemento = int(input(f"Digite o elemento {i+1}: "))
    lista2.append(elemento)

conjunto_uniao = set(lista1).union(lista2)

print("Conjunto da união:", conjunto_uniao)
