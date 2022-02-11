"""
8) Escreva um programa que leia 10 números e escreva o menor
valor lido e o maior valor lido.
"""

smaller = 0
bigger = 0
for num in range(1, 11):
        number = int(input(f'Enter the {num}º value: '))

        if smaller == 0 and bigger == 0:
                smaller = number
                bigger = number

        elif smaller > number:
                smaller = number

        elif bigger < number:
                bigger = number
print()
print(f'Smallest number is {smaller}')
print(f'Higher number is {bigger}')
