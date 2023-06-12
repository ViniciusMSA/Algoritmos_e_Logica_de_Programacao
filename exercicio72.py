#Faça a implementação de uma função recursiva que calcule a sequência de Fibonacci, recebendo como parâmetro o número de elementos da sequência.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequencia = fibonacci(n-1)
        sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia

n = int(input("Digite a quantidade de elementos da sequencia de fibonacci: "))
sequencia = fibonacci(n)
print("Sequência de Fibonacci:", sequencia)
