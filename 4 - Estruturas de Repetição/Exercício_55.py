"""
55) Escreva um programa que leia um inteiro não negativo n e imprima a soma
dos n primeiros números primos.
"""

number = int(input("Enter the value: "))

print()
if number > 0:
    soma = 0
    cont_primos = 1
    cont_qtd = 0

    for i in range(1, number ** 3):
        cont = 0
        for j in range(1, i+1):
            if (i % 1 == 0) and (i % j == 0):
                cont += 1

        if cont_primos <= number:
            if cont <= 2:
                soma += i
                cont_primos += 1
                cont_qtd += 1

        else:
            break

    print(f"The sum of the {number} first prime numbers is {soma}")
    print(cont_qtd)

else:
    print("Invalid Number")
