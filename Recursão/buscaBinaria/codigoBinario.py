def checkBits(num, lista):
    if num == 0:
        pass
    else:
        resultado = num // 2
        bit = num % 2
        lista.insert(0, str(bit))
        checkBits(resultado, lista)
    return lista


def escolhaDirecao(linha, num, ordens):
    posicao = -1
    linhaNova = []
    listaPos = []
    comando = ''
    if len(linha) == 1:
        if ordens[-1] != 'Meio':
            comando = 'Meio'
            ordens.append(comando)
        return ordens
    else:
        if len(linha) % 2 == 0:
            metade = int(len(linha) / 2)
            par = True
        else:
            metade = int((len(linha) - 1) / 2)
            par = False
        for i in range(len(linha)):
            if int(linha[i]) == int(num):
                posicao = i
                listaPos.append(posicao)
        if len(listaPos) > 1:
            if len(listaPos) % 2 == 0:
                posicao = listaPos[int(len(listaPos) / 2)]
            elif len(listaPos) % 2 == 1:
                posicao = listaPos[int((len(listaPos) + 1) / 2) - 1]
        if posicao == metade:
            comando = 'Meio'
            linhaNova = linha[int(metade)]
            ordens.append(comando)
        elif posicao > metade:
            comando = 'Direita'
            if par == False:
                for i in range(1, int(metade) + 1):
                    linhaNova.append(linha[i + int(metade)])
            else:
                for i in range(1, int(metade)):
                    linhaNova.append(linha[i + int(metade)])
            ordens.append(comando)
            escolhaDirecao(linhaNova, num, ordens)
        elif posicao < metade:
            comando = 'Esquerda'
            for i in range(0, int(metade)):
                linhaNova.append(linha[i])
            ordens.append(comando)
            escolhaDirecao(linhaNova, num, ordens)
    return listaComandos



linha = input()
linhas = []
linhase = linha.split(' ')
for i in range(len(linhase)):
    linhaca = int(linhase[i])
    linhas.append(linhaca)
linhas.sort()
escolha = int(input())
bits = int(input())
listaComandos = []
listaBits = []
comandos = ''

if escolha in linhas:
    listaBits = checkBits(escolha, listaBits)
    listaComandos = escolhaDirecao(linhas, escolha, listaComandos)
    if len(listaBits) > bits:
        print('Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')
    if len(listaBits) < bits:
        add = bits - len(listaBits)
        for i in range(add):
            listaBits.insert(0,'0')
    if len(listaBits) == bits and len(listaBits) != 0:
        bites = ''.join(listaBits)
        if len(listaComandos) > 1:
            for i in range(len(listaComandos) - 1):
                comandos += f'{listaComandos[i]} -> '
            comandos = f'{comandos}{listaComandos[len(listaComandos)-1]}'
        else:
            comandos = listaComandos[0]
        print(f'{comandos}, seguindo por essas coordenadas você vai chegar no número {bites}.')
    elif len(listaBits) == 0:
        print('Consegui encontar a saída, mas não consigo falar pois o número é muito grande para essa quantidade de bits.')

else:
    if escolha < int(linhas[0]) or escolha > int(linhas[len(linhas)-1]):
        print('Acho que a Doutora se confundiu, pois é impossível chegar nesse número pois ele é menor que a menor sala ou maior que o maior da sala.')
    elif escolha > int(linhas[0]) and escolha < int(linhas[len(linhas)-1]):
        num = 0
        number = 1000000
        guarda = int()
        for i in range(len(linhas)):
            num = escolha / int(linhas[i])
            if num < number and num > 1:
                number = num
                guarda = linhas[i + 1]
        listaBits = checkBits(escolha, listaBits)
        listaComandos = escolhaDirecao(linhas, guarda, listaComandos)
        if len(listaBits) > bits:
            print('Busquei muito, mas não achei a sala, que nem posso dizer, já que tenho poucos bits.')
        if len(listaBits) < bits:
            add = bits - len(listaBits)
            for i in range(add):
                listaBits.insert(0, '0')
        if len(listaBits) == bits:
            bites = ''.join(listaBits)
            if len(listaComandos) > 2:
                for i in range(len(listaComandos) - 1):
                    comandos += f'{listaComandos[i]} -> '
                comandos = f'{comandos}{listaComandos[len(listaComandos) - 1]}'
            else:
                comandos = listaComandos[0]
            print(f'{comandos}, mas não consegui achar.')
