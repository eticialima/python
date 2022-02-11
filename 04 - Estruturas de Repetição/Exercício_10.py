"""
10) Faça um programa que calcule e mostre a soma dos 50
primeiros números pares.
"""

number = 50
count = 0
even_sum = 0

for n in range(1, 1000):
        if n % 2 == 0:
                print(n)
                even_sum += 1
                count += 1

        if count == 50:
                break

print(even_sum)
