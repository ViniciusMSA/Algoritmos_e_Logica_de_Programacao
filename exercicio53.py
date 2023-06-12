#Faça um algoritmo que armazenará os 10 primeiros números primos acima de 100. Ao final, o algoritmo deve mostrar os valores desse vetor.

primos = []
num = 101

while len(primos) < 10:
    eh_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            eh_primo = False
            break
    if eh_primo:
        primos.append(num)
    num += 1

print("Os 10 primeiros números primos acima de 100 são:")
for primo in primos:
    print(primo)
