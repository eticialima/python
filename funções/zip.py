# Cria duas listas, uma com os nomes das frutas e outra com os preços
nomes = ["maçã", "banana", "laranja", "manga"]
precos = [2.5, 1.5, 3.0, 4.0]

# Usa a função zip para juntar as duas listas
for nome, preco in zip(nomes, precos):
    # Imprime o nome e o preço da fruta
    print(nome, "custa R$", preco)


# Cria três listas, uma com nomes de frutas, outra com preços e outra com quantidades
nomes = ["maçã", "banana", "laranja", "manga"]
precos = [2.5, 1.5, 3.0, 4.0]
quantidades = [10, 20, 30, 40]

# Usa a função zip para juntar as três listas
for nome, preco, quantidade in zip(nomes, precos, quantidades):
    # Calcula o valor total de cada fruta
    valor_total = preco * quantidade
    # Imprime o nome, preço e quantidade da fruta, além do valor total
    print(nome, "custa R$", preco, "e há", quantidade, "disponíveis. Valor total: R$", valor_total)


## Para lista com quantidades de itens diferentes
lista1 = [1, 2, 3, 4, 5]
lista2 = ['A', 'B', 'C']

resultado = list(zip(lista1, lista2))

print(resultado)
# Output: [(1, 'A'), (2, 'B'), (3, 'C')]
