#Elabore um algoritmo para determinar quantas vogais existem dentro de uma determinada frase (que deve ser recebida do usuario)

contador = 0

frase = input("Digite uma frase: ")
for i in frase:
    if i.lower() in "AaEeÉéIiOoUu":
        contador = contador + 1
print(f"Na frase digitada existem {contador} vogais.")
