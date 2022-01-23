"""
14) Faça um programa que leia um vetor de 10 posições e verifique se existem
valores iguais e os escreva na tela.
"""

lista = []
checks = []

for i in range(10):
    lista.append(int(input("Enter the value: ")))

    if lista[i] in checks:
        print(f"The value {lista [i]} already exists in the vector")

    checks.append(lista[i])

print(checks)
