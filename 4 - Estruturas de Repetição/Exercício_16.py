"""
16) Faça um programa que leia um número inteiro positivo impar N
imprima todos os núemros impares de 1 até N em ordem decrescente.
"""

number = int(input("Enter a positive and odd number: "))

print()

if number % 2 == 1:
        print(f'All odd numbers from 1 to {number} in ascending order: ')
        for n in range(number + 1, - 1, - 1):
                if n % 2 == 1:
                        print(n)
else:
        print('Enter a positive and odd number..Please!')
