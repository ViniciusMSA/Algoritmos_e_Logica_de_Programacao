#Faça um algoritmo que carregue um dicionário de 10 elementos onde a chave é o sobrenome da pessoa e o valor a sua idade. Após a finalização da entrada, o algoritmo deve escrever o sobrenome da pessoa com maior idade.

dicionario = {}
for i in range(10):
    sobrenome = input("Digite o sobrenome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    dicionario[sobrenome] = idade

sobrenome_maior_idade = max(dicionario, key=dicionario.get)

print("Sobrenome da pessoa com maior idade:", sobrenome_maior_idade)
