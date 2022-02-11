"""
42) Faça um programa que leia um conjunto não determinado de valores,
um de cada vez, e escreva para cada um dos valores lidos, o quadrado
o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
"""

while True:
    number = int(input("Enter the value: "))

    print()
    if number > 0:
        print(f"The square of {number}: {number ** 2}")
        print(f"The cube of {number}: {number ** 3}")
        print(f"The square root of {number}: {number ** (1/2)}")

        print()

    else:
        print("Value cannot be negative or zero!")
        break
