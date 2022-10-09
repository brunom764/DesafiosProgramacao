n = int(input(''))
numeroDeDistancias = n - 1
contador = 0
somaDistancias = 0
ePrimo = 0
checkPrimo = False
numEstrela1 = 1
numEstrela2 = 2
membroSeq1 = 0
membroSeq2 = 1
seq = 0
checkSequencia = False

if n <= 0:
    print('Isso está quebrado, acho que Howard pode me ajudar.')
elif 0 < n < 3:
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')
else:
    X1 = int(input(''))
    Y1 = int(input(''))
    for i in range(0, n - 1):
        X2 = int(input(''))
        Y2 = int(input(''))

        distancia = int(((X1 - X2) ** 2 + (Y1 - Y2) ** 2) ** 0.5)
        print(f'Distância [star{numEstrela1} <-> star{numEstrela2}]: {distancia}')
        somaDistancias += distancia

        numEstrela1 += 1
        numEstrela2 += 1

        X1 = X2
        Y1 = Y2

        while seq < distancia:
            seq = membroSeq1 + membroSeq2
            membroSeq1 = membroSeq2
            membroSeq2 = seq
            if seq == distancia:
                checkSequencia = True
                print('ficou true')


        if checkSequencia == True:
            contador += 1
        else:
            pass

    for i in range(2, somaDistancias):
        if somaDistancias % i == 0:
            ePrimo += 1


    if ePrimo == 0:
        checkPrimo = True


    if contador == numeroDeDistancias and checkPrimo == True:
        print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
    elif contador == numeroDeDistancias and checkPrimo == False:
        print('Yes! Eu consegui!')
    elif contador == numeroDeDistancias - 1:
        print('Oh, não! Eu quase consegui!')
    elif contador <= numeroDeDistancias - 2 and checkPrimo == False:
        print('Eu vou acabar como o Stuart :/')
    elif contador <= numeroDeDistancias - 2 and checkPrimo == True:
        print('Pelo menos o programa está funcionando...')



















