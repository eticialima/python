# Define uma lista de preços de frutas
precos_frutas = [2.99, 1.99, 3.49, 2.49, 1.5]

# Ordena a lista de preços em ordem crescente usando sorted()
precos_frutas_ordenados = sorted(precos_frutas)
print("Preços de frutas ordenados:", precos_frutas_ordenados)

# Imprime as frutas disponíveis com seus respectivos preços ordenados
frutas = ["maçã", "banana", "laranja", "pera", "uva"]
for i in range(len(frutas)):
    print(f"{frutas[i]}: {precos_frutas_ordenados[i]}")
