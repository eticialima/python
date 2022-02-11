"""
36) Leia um vetor com 10 números reais, ordene os elementos deste valor,
e no final escreva os elementos do vetor ordenado.
"""

lista = []

for i in range(10):
    lista.append(float(input("Enter a decimal number: ")))

lista.sort()

print(f"\nOrdered vector: {lista}")
