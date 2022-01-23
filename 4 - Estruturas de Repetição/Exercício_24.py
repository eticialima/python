"""
24) Escreva um porgrama que leia um número inteiro e calcule a
soma de todos os divisores desse número, com exceção dele próprio.
Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""

number = int(input("Enter the number: "))
soma = 0

print()
if number > 0:
        for n in range(1, number):
                if number % n == 0:
                        soma += n
        print(f"The sum of the number divisors {number} is {soma}")

elif number < 0:
        for n in range(number + 1, 0, 1):
                if number % n == 0:
                        print(n)
                soma += n

        print(f"The sum of the number divisors {number} is {soma}")

else:
    print("The number must be zero!")
