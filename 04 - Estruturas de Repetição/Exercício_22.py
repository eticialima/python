"""
22) Escreva um programa completo que permita a qualquer aluno
introduzir, pelo teclado, uma sequência arbitrária de notas(válidas no intervalo de
10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética.
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido
ao programa, o qual terminará quando for introduzido um valor que não seja válido
como nota de aprovação.
"""

note = 0.0

soma = 0.0
cont = 0
while True:
        note = float(input("Enter a note between 10 and 20: "))

        if (note >= 10) and (note <= 20):
                soma += note
                cont += 1

        else:
                if cont == 0:
                        cont += 1
                print(f"Invalid {note} note!")
                break

print()
print("Arithmetic mean:% .1f (excluding the last note entered)" % (soma / cont))
