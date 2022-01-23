"""
27) Em Matemática, o número harmônico designado por H(n) define-se
como sendo a soma da série harmônica:
    H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""

number = int(input("Enter an integer and positive value: "))

h = 1

if number > 0:
        for i in range(1, number + 1):
                h += 1 / i

        print(f"The value of H(n): {h}")

else:
        print("Value must be positive!")
