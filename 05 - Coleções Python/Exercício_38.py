"""
38) Peça ao usuário para digitar dez valores numéricos e ordene por ordem
crescente esses valores, guardando-os num vetor. Ordene o valor assim
que ele for digitado. Mostre ao final na tela os valores em ordem.
"""

lista = []

for i in range(10):
    lista.append(int(input("Enter a number: ")))
    lista.sort()

print(f"\nAscending vector: {lista}")
