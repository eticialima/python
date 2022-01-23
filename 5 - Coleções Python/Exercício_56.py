"""
56) Leia uma matriz 10 x 3 com as notas de 10 alunos.txt em 3 provas. Em
seguida, escreva o número de alunos.txt cuja pior nota foi na prova 1, o número
de alunos.txt cuja pior nota foi na prova 2, e o número de alunos.txt cuja pior
nota foi na prova 3. Em caso de empate das piores notas de um aluno,
o critério de desempate é arbitrário, mas o aluno
deve ser contabilizado apenas uma vez.
"""

alunos = []

for i in range(10):

    provas = []
    for j in range(3):
        prova = float(input(f"Enter the grade of the student's {j + 1} ° exam {i + 1}: "))
        provas.append(prova)
    alunos.append(provas)

    print()

quantidade = [0, 0, 0]

for i in range(10):
    for j in range(3):
        # Com o break, o aluno será contabilizado com a menor nota em uma das provas
        # apenas uma vez
        if min(alunos[i]) == alunos[i][j]:
            quantidade[j] += 1
            break

for i in range(3):
    print(f"The number of students.txt with the lowest grade in the test {i + 1}: {quantidade[i]}")
