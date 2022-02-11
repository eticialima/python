"""
28) Faça um porgrama que leia um valor N inteiro e positivo,
calcule e mostre o valor E, conforme a fórmula a seguir
    E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""
number = int(input("Digite um valor inteiro e positivo: ")) 
e = 1

print()
if number > 0:
        for n in range(1, number + 1):
                        fatores = n 
                for j in range(1, fatores):
                        fatores *= j 
                        e += 1/fatores

        print(f"The value of E = {e}")

else:
        print("Value must be positive!")
