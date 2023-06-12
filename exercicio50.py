#Faça um algoritmo que leia 20 palavras de no máximo 10 caracteres, e após a leitura, realize um processo qualquer que inverta os caracteres de cada uma das palavras.

palavras = []

print("Digite as 20 palavras:")
for i in range(20):
    palavra = input("Digite uma palavra: ")
    palavras.append(palavra)

for i in range(20):
    palavras[i] = palavras[i][::-1]

print("\nPalavras invertidas:")
for palavra in palavras:
    print(palavra)
