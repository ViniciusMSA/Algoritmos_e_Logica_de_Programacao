#Escreva um algoritmo que receba tres notas de um aluno, calcule e mostre a media aritmetica e a mensagem
#que segue a tabela abaixo. Para alunos de exame, calcule e mostre a nota que devera ser tirada no
#exame para aprovação, considerando que a média do exame é 6.0.(e que a media apos o exame é resultado
#da media aritmetica entre a nota do exame e a media antes do exame)

#0,0 < 3,oo         --- Reprovado
#>= 3,00 e < 7,00   --- Exame
#>= 7,00 e <= 10,00 --- Aprovado

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = (nota1 + nota2 + nota3) / 3
print("A sua media foi de", media)
if media > 0 and media < 3:
    print("Sua media foi inferior a tres. Voce esta reprovado.")
elif media >= 3 and media < 7:
    print("A sua media foi inferior a sete. Voce esta de exame.")
else:
    print("Parabens, sua média foi maior do que seis. Voce esta aprovado.")