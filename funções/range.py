## Como usar o Range.py

## Criar um simples menu de itens com função range()

# Define uma lista de itens de menu
menu_items = ["Pizza", "Hambúrguer", "Frango", "Salada", "Sopa"]

# Usa range() para iterar sobre os índices dos itens de menu
for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]}")

# Solicita ao usuário selecionar um item de menu
selecionado = int(input("Selecione um item de menu (número): "))

# Imprime o item de menu selecionado
print(f"Você selecionou: {menu_items[selecionado-1]}")

