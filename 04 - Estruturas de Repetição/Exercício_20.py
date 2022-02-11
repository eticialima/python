"""
20) Ler uma sequência de números inteiros e determinar se eles são pares
ou não. Deverá ser informado o número de dados lidos e números de valores
pares. O processo termina quando for digitado o número 1000.
"""

number = 0
cont_numbers = 0
cont_pair = 0

while number != 1000:
        number = int(input("Please enter a number: "))

        if (number > 0) and (number % 2 == 0) or (number < 0) and (number % 2 == -1):
                cont_pair += 1

        cont_numbers += 1

print()
print(f"Number of data read: {cont_numbers}")
print(f"Number of even values: {cont_pair}")


