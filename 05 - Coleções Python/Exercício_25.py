"""
25) Faça um programa que preencha um vetor de tamanho 100
com os 100 primeiros naturais que não são múltiplos de 7 ou
que terminam com 7.
"""

vector = []

for n in range(1, 100 ** 5):

    if len(vector) >= 100:
        break

    else:
        number = str(n)

        if (not (n % 7 == 0)) or number[len(number) - 1] == '7':
            vector.append(n)

print(vector)
