#Faça um algoritmo para ler nove caracteres numéricos em uma string. Mostre o conteudo dessa string colocando pontos e virgula, respectivamente nas posições inteiras e decimais.

#Exemplo: 
#Digitado -> 987654321
#Mostrado -> 9.876.543,21

numero = input("Digite um número de nove dígitos: ")

if len(numero) != 9:
    print("Número inválido. Digite um número com nove dígitos.")
else:
    numeroFormatado = f"{numero[:1]}.{numero[1:4]}.{numero[4:7]},{numero[7:]}"
    print("Numero formatad: ", numeroFormatado)




