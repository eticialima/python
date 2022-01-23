 
# Sequência de Fibonacci


# Função usando listas 449MB


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste 1
for n in fib_lista(100000):
    print(n)


# Função usando geradores 3MB


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 Gearadores
for n in fib_gen(100000):
    print(n)
 