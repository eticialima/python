"""
21) Faça um programa que receba dois números. Calcule e mostre:
    - A soma dos números pares desse intervalo de números, incluindo
os números digitados;
    - A multiuplicação dos números ímpares desse intervalo, incluindo
os digitados;
"""

number_01 = int(input("Enter the first number: "))
number_02 = int(input("Enter the second number: "))

sum_pairs = 0
odd_multiplication = 1

if number_01 >= number_02:

        for i in range(number_02, number_01 + 1):
                if i % 2 == 0:
                        sum_pairs += i

                elif i % 2 == 1:
                        odd_multiplication *= i

                elif (i % 2 == -1) and (i < 0):
                        odd_multiplication *= i

                else:
                        print("Error!")

elif number_02 > number_01:
        for i in range(number_01, number_02 + 1):
                if i % 2 == 0:
                        sum_pairs += i

                elif i % 2 == 1:
                        odd_multiplication *= i

                elif (i % 2 == -1) and (i < 0):
                        odd_multiplication *= i

                else:
                        print("Error!")

print()
print(f"The sum of even numbers in the number range: {sum_pairs}")
print(f"The multiplication of odd numbers in the range of the numbers entered: {odd_multiplication}")
