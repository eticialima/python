"""
40) Elabore um programa que faça leitura de vários números inteiros, até que se
digite um número negativo. O programa tem que retornar o maior e o menor
número lido.
"""

number = int(input("Digite um número: "))

if number > 0:
    bigger = number
    smaller = number

    while number >= 0:
        number = int(input("Digite um número: "))

        if number < 0:
            break

        elif number > bigger:
            bigger = number

        elif number < smaller:
            smaller = number

    print()
    print(f"The smallest number entered is {smaller}")
    print(f"The largest number entered is {bigger}")

else:
    print("The number must be greater than or equal to zero")
