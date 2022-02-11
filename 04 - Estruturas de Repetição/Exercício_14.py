"""
14) Faça um programa que leia um número inteiro positivo par N e imprima
todos os números pares de 0 até N em ordem decrescente.
"""

number = int(input("Enter a positive and even number: "))

print()

if number % 2 == 0:
        print(f'All even numbers from 0 to {number}: ')
        for n in range(number + 1, - 1, - 1):
                if n % 2 == 0:
                        print(n)
else:
    print('Enter a positive and even number...Please!')
