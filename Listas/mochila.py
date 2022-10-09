numMochila = int(input())
nomes = str(input()).split()
listTamanhos = list()
mochilas = list()

for i in range(0, numMochila):
    tamanho = input()
    listTamanhos.append(tamanho)
    mochila = ["Lanterna", "Omega 3 da top therm"]
    mochilas.append(mochila)

quantidadeItens = int(input())
for m in range(0, quantidadeItens):
    objeto = str(input())
    localObjeto = int(input())
    if int(listTamanhos[localObjeto]) > len(mochilas[localObjeto]):
        mochilas[localObjeto].append(objeto)
    else:
        print('Mochila cheia. Não vai dar para levar.')

while True:
    acao = str(input())
    if acao == 'CHEGAMOS NO CIN!':
        break
    elif acao == 'Tirar da mochila':
        itemAcionado = str(input())
        mochilaAcionada = int(input())
        if itemAcionado in mochilas[mochilaAcionada]:
            print(f'{itemAcionado} usado com sucesso da mochila {mochilaAcionada}.')
            mochilas[mochilaAcionada].remove(itemAcionado)
        else:
            print(f'Você não tem {itemAcionado} na mochila {mochilaAcionada}.')
    elif acao == 'Guardar na mochila':
        itemAcionado = str(input())
        mochilaAcionada = int(input())
        if int(listTamanhos[mochilaAcionada]) > len(mochilas[mochilaAcionada]):
            print(f'{itemAcionado} adicionado na mochila {mochilaAcionada}.')
            mochilas[mochilaAcionada].append(itemAcionado)
        else:
            print(f'Mochila {mochilaAcionada} cheia!')
    else:
        print('Ação inválida.')


for n in range(0, numMochila):
    print(f'Mochila de {nomes[n]} chegou assim:')
    for item in mochilas[n]:
        print(item)

