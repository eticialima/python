"""
17) Leia um vetor de 10 posições e atribua valor 0
para todos os elemntos que possírem valores negativos.
"""

lista = []

for i in range(10):
    num = int(input("Enter the value: "))

    if num >= 0:
        lista.append(num)

    else:
        lista.append(0)

print(f"\nVetor: {lista}")
