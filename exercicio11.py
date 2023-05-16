#Sabe-se que:
#   1 pé    = 12 polegadas
#   1 jarda = 3 pés
#   1 milha = 1760 jardas
#Escreva um algoritmo que receba uma medida  em pés, faça as conversões a seguir e mostre os resultados:
#A) Polegas
#B) Jardas
#C) Milhas

medidaEmPes = float(input("Digite uma medida em pés:"))
medidaemPolegadas = medidaEmPes * 12
print("A medida em polegadas é:", medidaemPolegadas)
medidaEmJardas = medidaEmPes * 3
print("A medida em jardas é:", medidaEmJardas)
medidaemMilhas = medidaEmJardas * 1760
print("A medida em milhas é:", medidaemMilhas)
