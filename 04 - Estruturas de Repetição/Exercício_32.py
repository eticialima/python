"""
32) Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes,
e tem como saída o número de cada dado e a relação entre eles (>, <, =) de
cada lançamento
"""

from random import randint

number = int(input("Enter the number of times you want to roll the two dice: "))

d1 = 0
d2 = 0

for i in range(number):
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    print()
    print(f'Lançamento {i + 1}:')

    if d1 > d2:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 > Dado 2')

    elif d1 < d2:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 < Dado 2')

    else:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 = Dado 2')
