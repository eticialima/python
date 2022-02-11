"""
7) Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média
"""

count = 10
soma = 0
average = 0
for num in range(1, 11):
        number = int(input(f'Enter the {num}º value: '))
        if number < 0:
                count -= 1
        else:
                soma += number

        if number >= 10:
                average = soma / count
print()
print(f'Average: {average}')
