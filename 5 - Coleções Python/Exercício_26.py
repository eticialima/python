"""
26) Faça um programa que calcule o desvio padrão de um vetor
v contendo n = 10 números, onde m é a média do vetor.
    Desvio Padrão = raiz quadrada de ((E (v[i] - M)²) / n)
"""

lista = []

for i in range(10):
    lista.append(int(input("Enter the value: ")))

n = len(lista)
m = sum(lista) / n

square_distancia = 0
for i in lista:
    square_distancia += (i - m) ** 2

standard_deviation = (square_distancia / n) ** 0.5

print(f"\nThe standard deviation is {standard_deviation}")
