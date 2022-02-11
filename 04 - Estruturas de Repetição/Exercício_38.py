"""
38) Faça um programa que calcule o terno pitagórico a, b, c, para o qual
a + b + c = 1000. Um termo pitagórico é um conjunto de três números
naturais, a, b, c, para a qual,
    a² + b² = c²
Por exemplo,
    3² + 4² = 9 + 16 = 25 = 5²
"""

qtd = 700

for i in range(1, qtd + 1):
    a = 0
    b = 0
    c = 0
    for j in range(1, qtd + 1):
        a = j
        b = i
        c = (a ** 2 + b ** 2) ** 0.5

        if b > a:
            if (a + b + c) == 1000:

                print(f"value of 'a' = {a}")
                print(f"value of 'b' = {b}")
                print(f"value of 'c' = {int(c)}")
                print()
