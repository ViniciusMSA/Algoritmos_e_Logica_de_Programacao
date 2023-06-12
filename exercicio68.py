#Faça uma função que determine se um ano qualquer, no formato AAAA, é bissexto. A função retorna 1 se o ano é bissexto e 0(zero) se não.

def eh_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return 1 
    else:
        return 0 

ano = int(input("Digite um ano (AAAA): "))
resultado = eh_bissexto(ano)

if resultado == 1:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")
