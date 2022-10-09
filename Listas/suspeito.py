listaSuspeitos = list()
suspeitos = input('')
listaSuspeitos = suspeitos.split(',')
quantidadeDeSuspeitos = len(listaSuspeitos)
checkRemoveSuspeito = False
checkNovoSuspeito = False


while quantidadeDeSuspeitos > 1:
    entrada = input()
    if entrada == 'Não encontrei nada no primeiro suspeito':
        listaSuspeitos.pop(0)
    elif entrada == 'O último da lista está limpo':
        listaSuspeitos.pop(quantidadeDeSuspeitos - 1)
    elif entrada == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':
        if quantidadeDeSuspeitos + 1 % 2 == 0:
            listaSuspeitos.pop(round(quantidadeDeSuspeitos + 1 / 2))
        else:
            listaSuspeitos.pop(round(quantidadeDeSuspeitos / 2))
    elif entrada == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':
        checkRemoveSuspeito = True
    elif checkRemoveSuspeito and entrada.isnumeric():
        listaSuspeitos.pop(int(entrada))
        checkRemoveSuspeito = False
    elif entrada == 'Acho que temos mais uma opção a ser analisada...':
        checkNovoSuspeito = True
    elif checkNovoSuspeito and entrada.isalpha():
        listaSuspeitos.append(str(entrada))
        checkNovoSuspeito = False
    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')
    quantidadeDeSuspeitos = len(listaSuspeitos)

suspeito = listaSuspeitos[0]
print(f'Acho que encontramos o suspeito. O seu nome é {suspeito}, vamos salvar o Sam!')

