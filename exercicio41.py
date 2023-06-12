#Faça um algoritmo que solicite uma data no formato de uma string - dd/mm/aaaa. Mostre essa data no formato aaaa/mm/dd.

dia = input("Digite o dia: ")
mes = input("Digite o mes: ")
ano = input("Digite o ano: ")
data = ano + "/" + mes + "/" + dia
print(f"A data completa é: {data}")