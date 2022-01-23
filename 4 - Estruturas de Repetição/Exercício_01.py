"""
1) Faça um programa que determine e mostre os cincos primeiros
múltiplos de 3, considerando números maiores que 0
"""

count = 0
for number in range(1, 1000):
        if count >= 5:
                break

        if number % 3 == 0:
                print(number)
                count += 1
