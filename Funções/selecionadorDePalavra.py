
def outputMaisDeUmaSilaba(silabasSelecionadas):
    silabas = str()
    for i in range(0,len(silabasSelecionadas) - 1):
        silabas = f' {silabasSelecionadas[i]}, '
    silabas = f'{silabas + silabasSelecionadas[len(silabasSelecionadas) -1]}'
    print(f'Lembrei! As sílabas:{silabas} estão no nome do hospital. Obrigada, Totoro!')


def selecionaSilaba(silabasPalavra, palavra):
    silabas = ["shi", "chi", "ko", "ku", "ya", "ma"]
    palavrasComSilabas = ['shichi', 'shichiko', 'chiko', 'chikoku', 'koku', 'kokuya', 'kuya', 'kuyama', 'yama', 'shichikokuyama','chikokuyama', 'chikokuya', 'shichikokuya', 'shichikoku', 'kokuyama']
    temSilaba = maisDeUmaSilaba = repetido = False
    silabasSelecionadas = []
    silabaTida = str()
    if palavra in palavrasComSilabas:
        print(f'A palavra {palavra} está toda no nome do hospital. Acertou em cheio, Totoro!')
        for i in range(0, len(silabasPalavra)):
            if silabasPalavra[i] not in novaSilabas:
                novaSilabas.append(silabasPalavra[i])
    else:
        for silaba in range(0, len(silabasPalavra)):
            if silabasPalavra[silaba] in silabas and silabasPalavra[silaba] not in novaSilabas:
                novaSilabas.append(silabasPalavra[silaba])
                silabaTida = silabasPalavra[silaba]
                temSilaba = True
                silabasSelecionadas.append(silabasPalavra[silaba])
            elif silabasPalavra[silaba] in silabas and silabasPalavra[silaba] in novaSilabas:
                repetido = True
            if len(silabasSelecionadas) > 1:
                maisDeUmaSilaba = True
        if maisDeUmaSilaba:
            outputMaisDeUmaSilaba(silabasSelecionadas)
        elif not maisDeUmaSilaba and temSilaba:
            print(f'Lembrei! A sílaba {silabaTida} está no nome do hospital. Obrigada, Totoro!')
        elif repetido:
            pass
        else:
            print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")
    if sorted(novaSilabas) == sorted(silabas):
        print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
        exit()



def separaSilaba(palavra):
    silabasPalavra = []
    palavraPreservada = palavra
    while len(palavra) > 1:
        letrasPalavra = ''
        if palavra[1] == "a" or palavra[1] == "e" or palavra[1] == "i" or palavra[1] == "o" or palavra[1] == "u":
            letrasPalavra = palavra[0:2]
            palavra = palavra[2:]
        elif palavra[2] == "a" or palavra[2] == "e" or palavra[2] == "i" or palavra[2] == "o" or palavra[2] == "u":
            letrasPalavra = palavra[0:3]
            palavra = palavra[3:]
        silabasPalavra.append(letrasPalavra)
    selecionaSilaba(silabasPalavra, palavraPreservada)


palavraIncompleta = True
novaSilabas = []

while palavraIncompleta:
    palavra = str(input())
    separaSilaba(palavra)




