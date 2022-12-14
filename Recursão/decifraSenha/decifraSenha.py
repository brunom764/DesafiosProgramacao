def fib(n, repeticoes, resultado, resultadoAnterior, listFib):
    if repeticoes == 0:
        return listFib
    else:
        resultadoNovo = 0
        if (n == 0):
            resultado = 0
            resultadoNovo = 1
        elif (n == 1):
            resultado = 1
            resultadoNovo = 2
        else:
            resultadoNovo = resultado + resultadoAnterior
        listFib.append(resultadoNovo)
        listFib = fib(resultadoNovo, repeticoes - 1, resultadoNovo, resultado, listFib)
        return listFib


def fat(contador):
    if contador == 0:
        return 1
    else:
        if (contador == 1):
            return 1
        else:
            resultadoNovo = contador * fat(contador - 1)
        return resultadoNovo


def criaListFat(num, lista):
    fatNum = 1
    if num == 1:
        lista.append(num)
    for numero in range(1, 11):
        fatNum *= numero
        if fatNum == num:
            break
        lista.append(fatNum)

    return lista


def unirFrase(listFib, listFat):
    caracteres = []
    caractere = ''
    if len(listFib) % 2 == 0:
        for i in range(0,len(listFib)):
            num = (listFib[i] + listFat[i]) % 26
            caractere = chr(num + 97)
            print(f' {listFib[i]} + {listFat[i]} ={num} = {caractere}')
            caracteres.append(caractere)
    else:
        for i in range(0, len(listFib)):
            num = (listFib[i] * listFat[i]) % 26
            caractere = chr(num + 97)
            print(f' {listFib[i]} * {listFat[i]} = {num} = {caractere}')
            caracteres.append(caractere)
    return caracteres

def checkAlfabeto(letra):
    numLetra = ord(letra) - 97
    modLetra = numLetra % 11
    if modLetra == 0:
        letras = '1'
    elif modLetra == 1:
        letras = 'a'
    else:
        num = 0
        listFib = [0,1]
        listFat = [1]
        letras = []
        if modLetra - 2 > 0:
            listFib = fib(num, modLetra - 2, num, num, listFib)
        resulFat = fat(modLetra)
        listFat = criaListFat(resulFat, listFat)
        letras = unirFrase(listFib, listFat)
        letras = ''.join(letras)
    return letras


senha = str(input()).strip().lower()
palavrasQuantidade = int(input())
checkSenha = False

for i in range(palavrasQuantidade):
    palavra = input()
    senhaPalavra = []
    senhaPalavras = ''
    for i in range(len(palavra)):
        senhaLetras = checkAlfabeto(palavra[i])
        senhaPalavra.append(senhaLetras)
    for senhas in senhaPalavra:
        senhaPalavras += senhas
    print(senhaPalavras)
    if senhaPalavras.strip() == senha:
        checkSenha = True

if checkSenha:
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais.')


