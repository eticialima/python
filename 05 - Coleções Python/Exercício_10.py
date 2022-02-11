"""
10) Faça um programa para ler a nota da prova de 15 alunos.txt e armazene num vetor,
calcule e imprima a média geral.
"""

lista = []

for i in range(15):
    lista.append(float(input(f"Enter the grade of the {i + 1} ° student: ")))

print("\nThe overall average of students.txt: %.1f" % (sum(lista) / len(lista)))
