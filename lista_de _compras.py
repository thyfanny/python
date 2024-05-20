"""Lista de compras usando listas
   O usuário deve conseguir inserir, remover e listar"""

print('o seguinte programa é encerrado ao usuário digitar "sair"')
lista_compras = []
entrada = ''

while True:
    entrada = input("[1]adicionar, [2]remover ou [3]listar? ")
    if entrada == 'sair': break
    if entrada == '1':
        novo_item = input('item a ser inserido: ')
        lista_compras.append(novo_item)
        continue
    elif entrada == '2':
        index = input('indice do item a ser removido: ')
        index = int(index)
        if index < len(lista_compras) and index > len(lista_compras):
            print("valor de índice inválido")
            continue
        lista_compras.pop(index)
    elif entrada == '3':
        count = 0
        for item in lista_compras:
            print(f'{count} {item}')
            count+=1
    else:
        print("operação inválida")