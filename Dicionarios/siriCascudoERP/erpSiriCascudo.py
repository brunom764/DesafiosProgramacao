def novoPedido(pedido, dicPedido, cardapio, boolPedido, agrupa, sugLista):
    pedSug = {'nome': '', 'num': 0}
    if len(agrupa) > 0 and pedido in sugLista:
        for ped in agrupa:
            if pedido == ped['nome']:
                ped['num'] += 1
                pedSug = {'nome': ped['nome'], 'num': ped['num']}
                break
        if int(pedSug['num']) == 3:
            print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')
            cardapio = ('hamburguer de siri', 'pizza de siri', 'siri a parmegiana', 'siri frito', pedido)
            boolPedido = True
    else:
        dicPedido['num'] = 1
        dicPedido['nome'] = pedido
        agrupa.append(dicPedido.copy())
        sugLista.append(dicPedido['nome'])
    return cardapio, boolPedido, agrupa, sugLista


burguer = ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles')
cardapio = ('hamburguer de siri', 'pizza de siri', 'siri a parmegiana', 'siri frito')
pizza = ('siri', 'trigo', 'fermento', 'ovos', 'queijo')
parmeg = ('siri', 'trigo', 'ovos', 'queijo', 'tomate')
frito = ('siri', 'manteiga')
cardapioo = [{'nome': 'hamburguer de siri', 'chamado': 0, 'ingre:': burguer, 'valor': 24},
            {'nome': 'pizza de siri', 'chamado': 0, 'ingre:': pizza, 'valor': 42},
            {'nome': 'siri a parmegiana', 'chamado': 0, 'ingre:': parmeg, 'valor': 24},
            {'nome': 'siri frito', 'chamado': 0, 'ingre:': frito, 'valor': 15}]
sugesPedido = {'nome': '', 'num': 0}
blocSugesPedido = []
sugLista = []
pedidoList = ()
ingrePedidoNovo = ()
caixa = 40
siri = pao = alface = tomate = queijo = picles = 5
trigo = fermento = ovos = batata = arroz = manteiga = 5
tem = True
countBur = countPizza = countParmeg = countFrito = 0
continua = True
newPedido = False

while continua:
    tem = True
    try:
        if newPedido:
          ingrePedidoNovo = input().split(' ')
          newPedido = False
        else:
            pedido = input()
            if pedido not in cardapio:
                pedidoList = pedido.split(' ')
            if pedido == 'hamburguer de siri':
                siri -= 1
                pao -= 1
                alface -= 1
                tomate -= 1
                queijo -= 1
                picles -= 1
                caixa += 24
                countBur += 1
            elif pedido == 'pizza de siri':
                siri -= 1
                trigo -= 1
                fermento -= 1
                ovos -= 1
                queijo -= 1
                caixa += 42
                countPizza += 1
            elif pedido == 'siri a parmegiana':
                siri -= 1
                trigo -= 1
                ovos -= 1
                queijo -= 1
                tomate -= 1
                caixa += 24
                countParmeg += 1
            elif pedido == 'siri frito':
                siri -= 1
                manteiga -= 1
                caixa += 15
                countFrito += 1
            else:
                if pedido == cardapio[-1] and len(cardapio) > 4:
                  pedidoList = ingrePedidoNovo
                else:
                    for i in range(len(pedidoList)):
                        if pedidoList[i] not in burguer and pedidoList[i] not in pizza and pedidoList[i] not in parmeg and pedidoList[i] != 'arroz' and pedidoList[i] != 'batata':
                            tem = False
                if tem:
                    caixa += 5
                    if 'siri' in pedidoList:
                        siri -= 1
                        caixa += 8
                    if 'trigo' in pedidoList:
                        trigo -= 1
                        caixa += 3
                    if 'pao' in pedidoList:
                        pao -= 1
                        caixa += 2
                    if 'ovos' in pedidoList:
                        ovos -= 1
                        caixa += 2
                    if 'queijo' in pedidoList:
                        queijo -= 1
                        caixa += 5
                    if 'tomate' in pedidoList:
                        tomate -= 1
                        caixa += 2
                    if 'fermento' in pedidoList:
                        fermento -= 1
                        caixa += 2
                    if 'alface' in pedidoList:
                        alface -= 1
                        caixa += 1
                    if 'picles' in pedidoList:
                        picles -= 1
                        caixa += 3
                    if 'batata' in pedidoList:
                        picles -= 1
                        caixa += 4
                    if 'arroz' in pedidoList:
                        picles -= 1
                        caixa += 3
                else:
                    cardapio, newPedido, blocSugesPedido, sugLista = novoPedido(pedido, sugesPedido, cardapio, newPedido, blocSugesPedido, sugLista)
                    if not newPedido:
                        print(f'{pedido} ainda não é uma opção disponível.')
            if trigo == 0:
                trigo += 4
                caixa -= 12
            if siri == 0:
                siri += 4
                caixa -= 32
            if pao == 0:
                pao += 4
                caixa -= 8
            if ovos == 0:
                ovos += 4
                caixa -= 8
            if queijo == 0:
                queijo += 4
                caixa -= 20
            if tomate == 0:
                tomate += 4
                caixa -= 8
            if fermento == 0:
                fermento += 4
                caixa -= 8
            if alface == 0:
                alface += 4
                caixa -= 4
            if picles == 0:
                picles += 4
                caixa -= 12
            if arroz == 0:
                arroz += 4
                caixa -= 12
            if batata == 0:
                batata += 4
                caixa -= 16
            if tem:
                print(f'{pedido} saindo...')
    except EOFError:
      print('##### Fim do expediente #####')
      continua = False

print(f'O lucro obtido no dia de hoje foi de R${caixa - 40}.')
if countBur > countFrito and countBur > countPizza and countBur > countParmeg:
    print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')
elif countFrito > countBur and countFrito > countPizza and countFrito > countParmeg:
    print('Siri frito está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')
elif countPizza > countBur and countPizza > countFrito and countPizza > countParmeg:
    print('Pizza de siri está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')
elif countParmeg > countBur and countParmeg > countPizza and countFrito < countParmeg:
    print('Siri a parmegiana está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.')
else:
  pass