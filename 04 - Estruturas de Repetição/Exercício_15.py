"""
15) Faça um programa que leia um número inteiro positivo impar N e imprima
todos os números impares de 1 até N em ordem crescente.
"""

number = int(input("Enter a positive and odd number: "))

print()

if number % 2 == 1:
        print(f'All odd numbers from 1 to {number} in ascending order: ')
        for n in range(1, number + 1):
                if n % 2 == 1:
                        print(n)
else:
        print('Enter a positive and odd number..Please!')
