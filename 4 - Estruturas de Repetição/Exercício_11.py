"""
11) faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem crescente.
"""

number = int(input("Enter the Number: "))
soma = 0
if number > 0:
        for n in range(0, number + 1):
                print(n)
else:
    print("Enter a positive number please!")
