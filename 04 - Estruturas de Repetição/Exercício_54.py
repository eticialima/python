"""
54) Faça um programa que receba um número inteiro maior do que 1,
e verifique se o número fornecido é primo ou não.
"""

number = int(input("Enter the value: "))

cont = 0

if number > 1:
    for i in range(1, number + 1):
        if (number % 1 == 0) and (number % i == 0):
            cont += 1

    if cont <= 2:
        print("Prime number")

    else:
        print("Not a prime number")
