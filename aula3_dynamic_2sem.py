'''def inverter_rec(s):
    if len(s) <= 1:
        return s
    return inverter_rec(s[1:]) + s[0]

print(inverter_rec("Fiap"))

'''
import time

'''
# Contagem regressiva

def contagem_regresiva(n):
    if n == 0:
        return
    print(n)
    contagem_regresiva(n - 1)


# Teste
contagem_regresiva(8)


# Somas
def soma_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(soma_for(100))


def soma_loop(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


print(soma_for(100))


def soma_rec(n):
    if n == 1:
        return 1
    return n + soma_rec(n - 1)


print(soma_rec(100))

'''

#Memoizacao
#È uma tecnica para armazenar resultados ja calculos, evitando recomputacao/refazer o codigo inteiro para prosseguir.


'''#fatorial com memo
def fatorial(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * fatorial(n - 1, memo)
    return memo[n]

fatorial(5, memo=None)
'''
#so vai fazer diferenca com muitas repeticoes, muitas mesmo



#Exercicio
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    return fib(n - 1, memo) + fib(n - 2, memo)

print(fib(40, memo=None))

#versao melhor
def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
