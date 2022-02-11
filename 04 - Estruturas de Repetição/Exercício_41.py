"""
41) Faça um programa que calcula a associação em paralelo de dois resistores
R1 e R2 fornecidos pelo usuário via teclado. O programa fica pedindo estes
valores e calculando até que o usuário entre com um valor para resistência igual a zero.
    R = (R1 * R2) / (R1 + R2)
"""

while True:
    r = 0

    r1 = int(input("Enter the resistor value R1: "))
    if r1 != 0:
        r2 = int(input("Enter the resistor value R2: "))
        print()
        if r2 != 0:
            r = (r1 * r2) / (r1 + r2)
            print(f"Parallel association value of the resistors({r1} e {r2}):\n{r}")
            print()

        else:
            print("Value cannot be zero!")
            break

    else:
        print()
        print("Value cannot be zero!")
        break

