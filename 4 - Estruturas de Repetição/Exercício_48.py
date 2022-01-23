"""
48) Faça um programa que some os termos de valor par
da sequência de Fibonacci, cujos valores não ultrapassem quatro
milhões.
"""

sequence_01 = 0
sequence_02 = 1

soma = 0

for i in range(1_000_001):
    sequence_01 += sequence_02
    sequence_02 += sequence_01

    if (sequence_01 > 4_000_000) or (sequence_02 > 4_000_000):
        break

    if (sequence_01 % 2 == 0) and (sequence_01 <= 4_000_000):
        soma += sequence_01

    if (sequence_02 % 2 == 0) and (sequence_02 <= 4_000_000):
        soma += sequence_02

print(f"The sum of the even values that do not exceed four million: {soma}")
