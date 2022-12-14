def soma(termo1, termo2, termo3, matriz1, matriz2):
    guarda = int()
    if termo1 == "m1":
        termo1 = matriz1
        guarda = 1
    elif termo1 == "m2":
        termo1 = matriz2
        guarda = 2

    if termo2 == "m1":
        termo2 = matriz1
    else:
        termo2 = matriz2

    if termo3 == "m1":
        termo3 = matriz1
    else:
        termo3 = matriz2

    for i in range(0, len(termo2)):
        for j in range(0, len(termo2)):
            termo1[i][j] = int(termo2[i][j]) + int(termo3[i][j])
    ultimaOperacao = termo1
    if guarda == 1:
        matriz1 = termo1
    else:
        matriz2 = termo1
    return matriz1, matriz2, ultimaOperacao


def subtracao(termo1, termo2, termo3, matriz1, matriz2):
    if termo1 == "m1":
        termo1 = matriz1
        guarda = 1
    else:
        termo1 = matriz2
        guarda = 2

    if termo2 == "m1":
        termo2 = matriz1
    else:
        termo2 = matriz2

    if termo3 == "m1":
        termo3 = matriz1
    else:
        termo3 = matriz2

    for i in range(0, len(termo2)):
        for j in range(0, len(termo2)):
            termo1[i][j] = int(termo2[i][j]) - int(termo3[i][j])
    ultimaOperacao = termo1
    if guarda == 1:
        matriz1 = termo1
    else:
        matriz2 = termo1
    return matriz1, matriz2, ultimaOperacao


def multiplica(termo1, termo3, termo2, matriz1, matriz2):
    guarda = int()
    if termo1 == "m1":
        termo1 = matriz1
        guarda = 1
    elif termo1 == "m2":
        termo1 = matriz2
        guarda = 2

    if termo2.isnumeric()  == False:
        if termo2 == "m1":
            termo2 = matriz1
        elif termo2 == "m2":
            termo2 = matriz2
        if termo3.isnumeric():
            for i in range(0, len(termo2)):
                for j in range(0, len(termo2)):
                    termo1[i][j] = int(termo3) * int(termo2[i][j])
        else:
            if termo3 == "m1":
                termo3 = matriz1
            elif termo3 == "m2":
                termo3 = matriz2
            termo1 = []
            for i in range(len(termo2)):
                termo1.append([0] * len(termo3))
            for i in range(len(termo2)):
                for j in range(len(termo3)):
                    for k in range(len(termo3)):
                        termo1[i][j] = int(termo1[i][j]) + (int(termo2[i][k]) * int(termo3[k][j]))

    else:
        if termo3 == "m1":
            termo3 = matriz1
        elif termo3 == "m2":
            termo3 = matriz2
        for i in range(0, len(termo3)):
            for j in range(0, len(termo3)):
                termo1[i][j] = int(termo2) * int(termo3[i][j])

    ultimaOperacao = termo1
    if guarda == 1:
        matriz1 = termo1
    else:
        matriz2 = termo1
    return matriz1, matriz2, ultimaOperacao


tamanhoMatrizes = int(input())
matriz = []

for i in range(0, 2):
    for j in range(0, tamanhoMatrizes):
        linhaLista = input().split()
        matriz.append(linhaLista)

matriz1 = matriz[0:tamanhoMatrizes]
matriz2 = matriz[tamanhoMatrizes:]


quantidadeOperacoes = int(input())
contador = 0
ultimaOperacao = []

while contador < quantidadeOperacoes:
    contador += 1
    mr = str(input())
    comando = mr.split()
    if comando[3] == "+":
        matriz1, matriz2, ultimaOperacao = soma(comando[0], comando[2], comando[4], matriz1, matriz2)
    elif comando[3] == '-':
        matriz1, matriz2, ultimaOperacao = subtracao(comando[0], comando[2], comando[4], matriz1, matriz2)
    else:
        matriz1, matriz2, ultimaOperacao = multiplica(comando[0], comando[4], comando[2], matriz1, matriz2)

for linha in ultimaOperacao:
    print(*linha)