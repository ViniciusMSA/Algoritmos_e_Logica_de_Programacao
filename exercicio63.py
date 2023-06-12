#Faça um algoritmo que carregue uma tupla de 10 elementos numéricos inteiros. Após a finalização da entrada, o algoritmo deve escrever a mesma tupla, na ordem inversa de entrada.

tupla = ()
for i in range(10):
    elemento = int(input("Digite um número inteiro: "))
    tupla = tupla + (elemento,)

tupla_inversa = tuple(reversed(tupla))

print("Tupla original:", tupla)
print("Tupla na ordem inversa:", tupla_inversa)
