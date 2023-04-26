#Lista de compras 
#Voçe pode adcionar e eliminar os itens

print("Lista de compras:")

lista_de_compras = []

while True:
    item = input("ite um item para a lista de compras (ou digite 'fim' para encerrar): ")
    if item == "fim":
        break
    else:
        lista_de_compras.append(item)


for indice, item in enumerate(lista_de_compras):
    print(str(indice + 1) + ". " + item)

while True:
    itens_remover = input("Qual item deseja remover ou digite \"fim\" pra encerrar: ")
    if itens_remover == "fim":
        break
    else:
        if itens_remover in lista_de_compras:
            lista_de_compras.remove(itens_remover)
            print(itens_remover, "foi removido da compra")
        else:
            print("Item não encontrado")

for indice, item in enumerate(lista_de_compras):
    print(str(indice + 1) + ". " + item)




