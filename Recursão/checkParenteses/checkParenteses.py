def checkQuantidade(nome, n, contadorOpen, contadorClose):
    if n == len(nome):
        if contadorOpen == contadorClose:
            print("Essa sentença está com os parênteses balanceados, HOORAY!")
        elif contadorOpen > contadorClose:
            print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
        elif contadorOpen < contadorClose:
            print("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")
    else:
        if nome[n] == "(":
            contadorOpen += 1
        if nome[n] == ")":
            contadorClose += 1
        print(contadorOpen, contadorClose)
        checkQuantidade(nome, n+1, contadorOpen, contadorClose)


def checkParenteses(sentenca):
    n = contadorOpen = contadorClose = 0
    checkQuantidade(sentenca, n, contadorOpen, contadorClose)


numSentencas = int(input())

for i in range(numSentencas):
    equacao = input()
    checkParenteses(equacao)