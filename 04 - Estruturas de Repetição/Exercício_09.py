"""
9) Faça um programa que leia um número inteiro N e depois imprima
os N primeiros números naturais ímpares
"""

number = int(input("Enter a number: "))

odd_sum = 0
cont = 0
print()

for n in range(1, number * number):
        if n % 2 == 1:
                print(n)
                cont += 1

        if cont == number:
                break
