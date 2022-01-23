"""
32) Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma
que o usuário não informa elementos repetidos). Calcule e mostre os
vetores resultantes em cada caso abaixo:
    . Soma entre x e y: soma de cada elemento x com o elemento da mesma
    posição em y.
    . Produto entre x e y: multiplicação de cada elemento de x com o
    elemento da mesma posição em y.
    . Diferença entre x e y: todos os elementos de x que não existam em y.
    . Interseção entre x e y: apenas os elementos que aparecem nos dois vetores
    . União entre x e y: todos os elemntos de x, e todos os elementos de y
    que não estão em x.
"""

x = []
y = []

for n in range(5):
    x.append(int(input("Type a vector element x: ")))

print()
for n in range(5):
    y.append(int(input("Type a vector element y: ")))

set_x = set(x)
set_y = set(y)

soma = sum(set_x) + sum(set_y)

product = 1
for n in range(5):
    product *= (x[n] * y[n])

difference = set_x.difference(set_y)
intersection = set_x.intersection(set_y)
union = set_x.union(set_y)

print(f"\nSum between x and y: {soma}")
print(f"Product between x and y: {product}")
print(f"Difference between x and y: {difference}")
print(f"Intersection between x and y: {intersection}")
print(f"Union between x and y: {set}")
