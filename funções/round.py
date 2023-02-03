# Recebe o preço de um produto
preco = float(input("Informe o preço do produto: "))

# Recebe o número de parcelas para pagamento
num_parcelas = int(input("Informe o número de parcelas: "))

# Calcula o valor da parcela
valor_parcela = preco / num_parcelas

# Usa a função round para arredondar o valor da parcela para duas casas decimais
valor_parcela = round(valor_parcela, 2)

# Imprime o resultado
print("O valor da parcela é de R$", valor_parcela)
