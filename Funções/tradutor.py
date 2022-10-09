def tradutor(seqNumeros):
    letra = ''
    mensagem = True
    letras = []
    for i in range(0, len(seqNumeros)):
        num = int(seqNumeros[i])
        if 0 <= num <= 25:
            letra = chr(num + 97)
        elif 26 <= num <= 49:
            letra = chr(num + 71)
        elif 50 <= num <= 75:
            letra = chr(num + 15)
        elif 76 <= num <= 99:
            letra = chr(num - 11)
        elif num == 100:
            letra = ' '
        else:
            mensagem = False
        letras.append(letra)
    if mensagem:
        formarFrase(letras)
    else:
        print('Infelizmente os números nao dizem nada')


def formarFrase(letras):
    print(f'{"".join(letras)}')


seqNumeros = input().split(' ')
tradutor(seqNumeros)



