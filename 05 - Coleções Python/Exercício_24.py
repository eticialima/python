"""
24) Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura
em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do
aluno mais baixo e do mais alto, juntamente com suas alturas.
"""

dictionary = {}

for n in range(10):

    number = int(input(f"Enter the number of the {n + 1} ° student: "))

    # Checks whether the number entered is the number of an existing student
    # Verifica se o número digitado é o número de um aluno já existente
    if number in dictionary.keys():
        print("Existing number\n")
        continue

    # If the number entered does not exist, it will ask you to add the height
    # Se o número digitado não existe, vai pedr para adicioonar a altura
    else:
        height = float(input(f"Enter the height of the {n + 1} ° student: "))
        dictionary[number] = height

        print()

for number, height in dictionary.items():

    if dictionary[number] == min(dictionary.values()):
        print(f"tallest student - Number: {number}; height: {height}")

    elif dictionary[number] == max(dictionary.values()):
        print(f"Tallest student - Number: {number}; height: {height}")
