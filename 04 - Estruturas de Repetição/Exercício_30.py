"""
30) Faça programas para calcular as seguintes sequências:
    1 + 2 + 3 + 4 + 5 + ... + n
    1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
    1 + 3 + 5 + 7 + ... + (2n - 1)
"""

terms = 10

calculation_01 = 0
calculation_02 = 0
calculation_03 = 0

for i in range(1, terms + 1):
        calculation_01 += i 
        if i == terms:
                if i % 2 == 0:
                        calculation_02 += -i + (2 * terms - 1) 
                elif i % 2 == 1:
                        calculation_02 += i + (2 * terms - 1)
                        calculation_03 += i 
                        calculation_03 += (2 * terms - 1) 
                break

        if i % 2 == 0:
                calculation_02 -= i

        elif i % 2 == 1:
                calculation_02 += i
                calculation_03 += i

print(calculation_01)
print(calculation_02)
print(calculation_03)

