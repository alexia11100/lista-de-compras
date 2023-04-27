print("Lista de Compras:")
itens = input("Digite os itens separados por ', ': ").split(", ")
for posicao in range(len(itens)):
    print(f"{posicao+1}. {itens[posicao]}")

print()

remover = input("Deseja remover algum item 'S' ou 'N'? ").upper()
if remover == "S":
    item = int(input("Escolha a posição do item: "))
    itens.pop(item-1)

for posicao in range(len(itens)):
    print(f"{posicao+1}. {itens[posicao]}")

print()