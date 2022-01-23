"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:

- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generators Functions (Funções Geradoras)

-------------------------------------------------------------------------------------
| Funções                                   | Generator Functions                   |
-------------------------------------------------------------------------------------
| Utilizam return                           | Utlizam yield                         |
-------------------------------------------------------------------------------------
| Retorna uma vez                           | Podem utilizar yield múltiplas vezes  |
-------------------------------------------------------------------------------------
| Quando executada, retorna um valor        | Quando executada, retorna um generator|
-------------------------------------------------------------------------------------
"""

# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok?


gen = conta_ate(5)

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


for num in gen:
    print(num)


# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok?


gen = conta_ate(10)

print(next(gen))  # 1

print('Geek')

for num in gen:
    print(num)


# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok?


gen = conta_ate(10)

print(list(gen))
 