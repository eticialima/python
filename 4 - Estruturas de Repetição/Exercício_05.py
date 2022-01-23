"""
5) Faça um programa que peça ao usuário para digitar
10 valores e some-os.
"""

soma = 0
for num in range(10):
        number = int(input(f'Enter the {num + 1} value: '))
        soma += number
print()
print(soma)
