#Exercicio repetido.
#O enunciado é exatamento o mesmo do exercicio 26.

#Faça um algoritmo que leia o valor do peso e da altura de 20 pessoas. Ao final, o algoritmo deve mostrar:

# -O peso médio
# -A altura média
# -O maior e o menor IMC

#Obs: IMC (Indice de Massa Corporal) calculado a partir da fórmula:

# IMC =       Peso
#      ------------------
#       (altura . altura)

somaPeso = 0.0
somaAltura = 0.0

#'inf' e '-inf' -> Representam o maior e o menor numero possivel em python.
maiorIMC = float('-inf') #Garante que o primeiro IMC calculado sera o maior! Se fosse inicializado com zero nao daria certo
menorIMC = float('inf') #Garante que o primeiro IMC calculado sera o menor! Se fosse inicializado com zero nao daria certo.

for i in range(1, 21):

    peso = float(input(f"Pessoa nª{i}: Digite quantos kilos voce pesa: "))
    somaPeso = somaPeso + peso

    altura = float(input(f"Pessoa nª{i}: Digite a sua altura: "))
    somaAltura = somaAltura + altura

    imc = peso / (altura ** 2)

    if imc > maiorIMC:
        maiorIMC = imc
    
    if imc < menorIMC:
        menorIMC = imc

mediaPeso = somaPeso / 20
mediaAltura = somaAltura / 20

print(f"A média de peso das 20 pessoas é: {mediaPeso}")
print(f"A média da altura das 20 pessoas é: {mediaAltura}")
print(f"O maior IMC das 20 pessoas é: {maiorIMC}")
print(f"O menor IMC das 20 pessoas é: {menorIMC}")