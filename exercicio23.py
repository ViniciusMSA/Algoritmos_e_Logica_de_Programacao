#Dados tres valores X, Y e Z, verifique se eles podem ser comprimentos dos lados de um triangulo e, se forem, verificar se é um triangulo equilátero, isósceles ou escaleno. Se eles formarem um triangulo, escrever uma mensagem.

#Considerar que:
#O comprimento de cada lado de um triangulo é menor do que a soma dos outros lados;
#Chama-se equilátero o triangulo que tem tres lados iguais;
#Chama-se isósceles o triangulo que tem o comprimento de dois lados iguais;
#Chama-se escaleno o triangulo que tem os tres lados diferentes;

print("Primeiro, precisamos da entrada de tres valores.")
x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))
z = float(input("Digite o terceiro valor: "))

print("Verificando se os valores digitados podem ser comprimentos dos lados de um triangulo.")
if x < (y + z) and y < ( x + z) and z < (x + y):
    print("Sim! Os valores digitados podem ser comprimentos dos lados de um triangulo!")
    print("Verificando o tipo do triangulo.")
    if x == y == z:
        print("O triangulo é equiátero: Os tres lados tem o mesmo valor!")
    elif x == y or x == z or y == z:
        print("O triangulo é isósceles: Pelo menos dois lados do triangulo sao iguais!")
    elif x != y != z:
        print("O triangulo é escaleno: Os tres lados do triangulo são diferentes!")
else:
    print("Não! Os valores digitados nao podem ser comprimentos dos lados de um triangulo!")

print("Fim do algoritmo!")