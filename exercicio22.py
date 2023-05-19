#Escreva um programa que receba o preço liquido de um produto e o seu codigo de origem e mostra
#a sua procedencia e o preço final, calculado pelo preço relativo a sua procedencia. A procedencia 
#obedece a tabela a seguir:

#Codigo de origem   #Procedencia    #% Imposto
#1                  #Sul            #11%
#2                  #Norte          #13%
#3                  #Nordeste       #9%
#4                  #Centro-Oeste   #12%
#5                  #Sudeste        #18%

codOrigem = int(input(
"""
Digite o codigo de origem do produto:
    1: Sul
    2: Norte
    3: Nordeste
    4: Centro-Oeste
    5: Sudeste
Código: 
"""))
reajustePreco = 0 #pela porcentagem do imposto.
precoProd = float(input("Digite o preço do produto: "))
if codOrigem == 1:
    print("A procedencia do produto é: Sul")
    reajustePreco = 0.11
    precoProd = precoProd * (1 + reajustePreco)
    print("O novo preço devido a procedencia do produto é:", precoProd)
elif codOrigem == 2:
    print("A procedencia do preoduto é: Norte")
    reajustePreco = 0.13
    precoProd = precoProd * (1 + reajustePreco)
    print("O novo preço devido a procedencia do produto é:", precoProd)
elif codOrigem == 3:
    print("A procedencia do produto é: Nordeste")
    reajustePreco = 0.09
    precoProd = precoProd * (1 + reajustePreco)
    print("O novo preço devido a procedencia do produto é:", precoProd)
elif codOrigem == 4:
    print("A procedencia do produto é: Centro-Oeste")
    reajustePreco = 0.12
    precoProd = precoProd * (1 + reajustePreco)
    print("O novo preço devido a procedencia do produto é:", precoProd)
else:
    print("A procedencia do produto é: Sudeste")
    reajustePreco = 0.18
    precoProd = precoProd * (1 + reajustePreco)
    print("O novo preço devido a procedencia do produto é:", precoProd)

