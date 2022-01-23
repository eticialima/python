"""
6) Faça um programa que leia 10 inteiros e imprima sua média.
"""

average = 0
for num in range(1, 11):
        number = int(input(f'Enter the {num}º value: '))
        average += number

        if num >= 10:
                average = average / num
print()
print(f'Average: {average}')
