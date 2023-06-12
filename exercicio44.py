#Faça um algoritmo para determinar quantas palavras existem em uma determinada frase. Obs: Tanto a palavra, quanto a frase, devem ser informadas pelo usuario.

frase = input("Digite uma frase: ")
palavras = frase.split()
quantidadePalavras = len(palavras)
print(f"Na frase digitada existem {quantidadePalavras} palavras.")
