"""
25) Faça um programa que some todos os números naturais abaixo de 1000
que são múltiplos de 3 ou 5.
"""

soma = 0

for n in range(1, 1000):
        if (n % 3 == 0) and (n < 1000) or (n % 5 == 0) and (n < 1000):
                soma += n

print(f"Sum of all natural numbers below 1000 that are multiples of 3 or 5: {soma}")
