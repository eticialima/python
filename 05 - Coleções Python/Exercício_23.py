"""
23) Ler dois conjuntos de números reais, armazenando-os em vetores
e calcular o produto escalar entre eles. Os conjuntos têm 5 elementos
cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto
escalar é dado por: x1 * y1 + x2 * y2 + ... + xn * yn
"""

lista1 = []
lista2 = []

for i in range(5):
    lista1.append(float(input("Enter a value for the first vector: ")))

print()
for i in range(5):
    lista2.append(float(input("Enter a value for the second vector: ")))

print(f"\nFirst vector: {lista1}")
print(f"Second vector: {lista2}")

produto_escalar = 0
for i in range(5):
    produto_escalar += (lista1[i] * (i + 1)) * (lista2[i] * (i + 1))

print(f"Scalar product of the two sets: {produto_escalar}")
