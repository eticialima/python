"""
46) Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar
acertar qual o número foi gerado, a cada tentativa o programa deverá informar se o
chute é menor ou maior que o número gerado. O programa acaba quando o usuário acerta
o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""
from random import randint

number = randint(1, 1000)

while True:
    attemp = int(input("Try to hit the random number: "))

    print()
    if attemp > number:
        print("The number is less. Try again!\n")

    elif attemp < number:
        print("The number is higher. Try again!\n")

    elif attemp == number:
        print("Congratulations, you got it right!")
        break
