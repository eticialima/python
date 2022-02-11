"""
17) Faça um programa que leia um número inteiro positivo
n e calcule a soma dos n primeiros números naturais.
"""

number = int(input("Enter an integer and positive number: "))
soma = 0
print()

if number > 0:
        print(f'The sum of the {number} first natural numbers')
        for n in range(1, number * number):
                if n <= number:
                        soma += n
                else:
                        break
        print(soma)
else:
        print('The number cannot be zero or negative!')
