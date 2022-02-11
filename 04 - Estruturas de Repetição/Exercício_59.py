"""
59) Escreva um programa que leia o número de habitantes de uma determinada cidade,
o valor do kwh, e para cada habitante entre com os seguintes dados: consumo do
mês e o código do consumidor (1-Residencial, 2-Comercial, 3-industrial). No final imprima
o maior, o menor e a média do consumo dos habitantes: e por fim o total do consumo de
cada categoria de consumidor.
"""

numero_habitantes = int(input("Enter the number of inhabitants of the city: "))

kwh = int(input("Enter the value of kwh: "))

menor = 0.0
maior = 0.0

residencial = 0.0
comercial = 0.0
industrial = 0.0

cont = 0

print()
for i in range(1, numero_habitantes + 1):
    consumo_mes = float(input(f"Enter the consumption of the month of the {i} inhabitant: "))
    codigo_consumidor = int(input(f"Enter the consumer code of the {i} inhabitant: "))

    if consumo_mes >= 0:

        if (codigo_consumidor >= 1) and (codigo_consumidor <= 3):

            cont += 1

            if i == 1:
                menor = consumo_mes

            if consumo_mes > maior:
                maior = consumo_mes

            elif consumo_mes < menor:
                menor = consumo_mes

            if codigo_consumidor == 1:
                residencial += consumo_mes

            elif codigo_consumidor == 2:
                comercial += consumo_mes

            elif codigo_consumidor == 3:
                industrial += consumo_mes

        else:
            print("Invalid code")

    else:
        print("Invalid consumption value")

    print()

total = residencial + comercial + industrial

print(f"The highest consumption was: {maior}")
print(f"The lowest consumption was: {menor}")
print("The average consumption was: %.2f\n" % (total / cont))
print(f"Total residential consumer consumption: {residencial}")
print(f"Total commercial consumer consumption: {comercial}")
print(f"Total industrial consumer consumption: {industrial}")
