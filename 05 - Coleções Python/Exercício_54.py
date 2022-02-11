"""
54) Leia uma matri 5z x 10 que se refere respostas de 10 quetões de
múltipla escolha, referentes a 5 alunos.txt. Leia também um vetor de
10 posições contendo o gabarito de respostas que podem ser a, b, c ou d.
Seu programa deverá comparar as respostas de cada candidato com o gabarito
e emitir um vetor denominado resultado, contendo a pontuação correspondente a cada
aluno.
"""

gabarito = []

cont = 0
while len(gabarito) < 10:
    resposta = str(input(f"Enter the correct question alternative {cont + 1}: "))

    if (resposta.lower() == 'a') or (resposta.lower() == 'b') or (resposta.lower() == 'c') or (resposta.lower() == 'd'):
        gabarito.append(resposta)

    else:
        print("Alternativa inválida")
        cont -= 1
    cont += 1

print()

alunos = []
for i in range(5):
    respostas = []
    for j in range(10):
        resposta = str(input(f"Type the alternative to the {j + 1} question for the {i + 1} student: "))

        if (resposta.lower() == 'a') or (resposta.lower() == 'b') or (resposta.lower() == 'c') or \
           (resposta.lower() == 'd'):
            respostas.append(resposta)

        else:
            # Caso o aluno digite uma alternativa inválida ou deixe em branco, a questão estará errada
            respostas.append('z')

    print()
    alunos.append(respostas)

resultado = {}
for i in range(5):
    corretos = 0
    for j in range(len(alunos[i])):
        if alunos[i][j] == gabarito[j]:
            corretos += 1

    resultado[f'student {i + 1}'] = corretos

for aluno, resultado in resultado.items():
    print(f"The {aluno} had {resultado} hits")
