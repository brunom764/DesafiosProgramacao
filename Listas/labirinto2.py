nome = input('')
linhas = []
linha = ''
linhaPersonagem = 0
colunaPersonagem = 0
linhaDermo = 0
colunaDermo = 0
linhaPortal = 0
colunaPortal = 0
vivo = True
fim = False
perdeu = False

goDireita = True
goBaixo = False
goCima = False
goEsquerda = False

goDireitaD = True
goBaixoD = False
goCimaD = False
goEsquerdaD = False

voltarHorizontalP = True
voltarVerticalP = True
voltarHorizontalD = True
voltarVerticalD = True

for l in range(0, 8):
    linha = input()
    linhas.append(list(linha))


for i in range(0, len(linhas)):
    for j in range(0, len(linhas[i])):
        if linhas[i][j] == "p":
            linhaPersonagem = i
            colunaPersonagem = j
        if linhas[i][j] == "d":
            linhaDermo = i
            colunaDermo = j
        if linhas[i][j] == "o":
            linhaPortal = i
            colunaPortal = j

while not fim:
    #personagem
    if linhas[linhaPersonagem][colunaPersonagem + 1] == "|" or linhas[linhaPersonagem][colunaPersonagem + 1] == "_" or linhas[linhaPersonagem][colunaPersonagem + 1] == "d" or voltarHorizontalP == False:
        goDireita = False
    else:
        goDireita = True

    if linhas[linhaPersonagem + 1][colunaPersonagem] == "_" or linhas[linhaPersonagem + 1][colunaPersonagem] == "|" or linhas[linhaPersonagem + 1][colunaPersonagem] == "d" or voltarVerticalP == False:
        goBaixo = False
    else:
        goBaixo = True

    if linhas[linhaPersonagem - 1][colunaPersonagem] == "_" or linhas[linhaPersonagem - 1][colunaPersonagem] == "|" or linhas[linhaPersonagem - 1][colunaPersonagem] == "d":
        goCima = False
    else:
        goCima = True

    if linhas[linhaPersonagem][colunaPersonagem - 1] == "|" or linhas[linhaPersonagem][colunaPersonagem - 1] == "_" or linhas[linhaPersonagem][colunaPersonagem - 1] == "d":
        goEsquerda = False
    else:
        goEsquerda = True

    #movimentoPersonagem
    if goDireita and voltarHorizontalP:
        linhas[linhaPersonagem][colunaPersonagem + 1] = "p"
        linhas[linhaPersonagem][colunaPersonagem] = "."
        colunaPersonagem += 1
        voltarVerticalP = True
    elif not goDireita and goBaixo:
        linhas[linhaPersonagem + 1][colunaPersonagem] = "p"
        linhas[linhaPersonagem][colunaPersonagem] = "."
        linhaPersonagem += 1
        voltarHorizontalP = True
    elif not goDireita and goCima:
        linhas[linhaPersonagem - 1][colunaPersonagem] = "p"
        linhas[linhaPersonagem][colunaPersonagem] = "."
        linhaPersonagem -= 1
        voltarVerticalP = False
        voltarHorizontalP = True
    elif not goBaixo and not goCima and goEsquerda:
        linhas[linhaPersonagem][colunaPersonagem - 1] = "p"
        linhas[linhaPersonagem][colunaPersonagem] = "."
        colunaPersonagem -= 1
        voltarVerticalP = True
        voltarHorizontalP = False
    elif not goDireita and not goBaixo and not goCima and not goEsquerda:
        linhas[linhaPersonagem][colunaPersonagem] = 'd'
        linhas[linhaDermo][colunaDermo] = '.'
        vivo = False
        fim = True
    if linhas[linhaPersonagem][colunaPersonagem] == linhas[linhaPortal][colunaPortal]:
        linhas[linhaPersonagem][colunaPersonagem] = "o"
        vivo = True
        fim = True

    #dermogodon
    if linhas[linhaDermo][colunaDermo + 1] == "|" or linhas[linhaDermo][colunaDermo + 1] == "_" or voltarHorizontalD == False:
        goDireitaD = False
    else:
        goDireitaD = True

    if linhas[linhaDermo + 1][colunaDermo] == "_" or linhas[linhaDermo + 1][colunaDermo] == "|" or voltarVerticalD == False:
        goBaixoD = False
    else:
        goBaixoD = True

    if linhas[linhaDermo - 1][colunaDermo] == "_" or linhas[linhaDermo - 1][colunaDermo] == "|":
        goCimaD = False
    else:
        goCimaD = True

    if linhas[linhaDermo][colunaDermo - 1] == "|" or linhas[linhaDermo][colunaDermo - 1] == "_":
        goEsquerdaD = False
    else:
        goEsquerdaD = True

    #movimentoDermogodon
    if fim:
        pass
    else:
        if goDireitaD and voltarHorizontalD:
            linhas[linhaDermo][colunaDermo + 1] = "d"
            linhas[linhaDermo][colunaDermo] = "."
            colunaDermo += 1
            voltarVerticalD = True
        elif not goDireitaD and goBaixoD and voltarVerticalD:
            linhas[linhaDermo + 1][colunaDermo] = "d"
            linhas[linhaDermo][colunaDermo] = "."
            linhaDermo += 1
            voltarHorizontalD = True
        elif not goDireitaD and goCimaD:
            linhas[linhaDermo - 1][colunaDermo] = "d"
            linhas[linhaDermo][colunaDermo] = "."
            linhaDermo -= 1
            voltarVerticalD = False
            voltarHorizontalD = True
        elif goEsquerdaD:
            linhas[linhaDermo][colunaDermo - 1] = "d"
            linhas[linhaDermo][colunaDermo] = "."
            colunaDermo -= 1
            voltarVerticalD = True
            voltarHorizontalD = False
        else:
            pass
        if linhas[linhaDermo][colunaDermo] == linhas[linhaPortal][colunaPortal]:
            linhas[linhaDermo][colunaDermo] = "o"
            perdeu = True
            fim = True


    #saida
    for i in range(0, 8):
        print(" ".join(linhas[i]))

if vivo and not perdeu:
    print(f'UFA!!! Você e {nome} conseguiram escapar do demodog e incendiar o subsolo, agora a Eleven vai conseguir fechar o portal.')
elif not vivo:
    print(f'Ah não, você e {nome} foram pegos pelo demodog e agora ele vai atravessar o portal e talvez a eleven não consiga salvar todos.')
elif perdeu:
    print(f'Ah não, você e {nome} não foram rápidos o bastante e o demodog passou pelo portal.')