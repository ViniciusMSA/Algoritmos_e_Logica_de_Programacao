#Elabore um algoritmo para ler/receber, separadamente, o primeiro nome, o nome do meio e o sobrenome de uma pessoa, e mostre o nome completo, correspondente.

nome = input("Digite o seu nome: ")
nomeMeio = input("Digite seu nome do meio: ")
sobrenome = input("Digite o seu sobrenome: ")
nomeCompleto = nome + " " + nomeMeio + " " + sobrenome + "!"
print(f"O seu nome completo é {nomeCompleto}")