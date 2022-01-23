"""
18) Escreva um algoritmo que leia certa quantidade de números
e imprima o maior deles e quantas vezes o maior número foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

number = int(input('Enter the number of numbers to be read: '))
bigger = 0
print()

for n in range(1, number + 1):
        num = int(input(f'Enter the {n} ° number:'))

        if n == 1:
                bigger = num
        elif num > bigger:
                bigger = num
print()
print(f'The largest number: {bigger}')
