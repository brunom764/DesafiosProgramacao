numeroMatriz = int(input())
linhas = []
membroMatriz = 0
maiorSomaLinha = 0
maiorSomaColuna = 0
maiorSomaDiagonal = 0
paresSomaLinha = 0
paresSomaColuna = 0
paresSomaDiagonal = 0

if numeroMatriz >= 2:
    for i in range(0, numeroMatriz):
        linha = input().split()
        linhas.append(linha)


    for linha in linhas:
        for i in range(0, len(linha) - 1):
            somaLinha = int(linha[i]) + int(linha[i + 1])
            if somaLinha > maiorSomaLinha:
                maiorSomaLinha = somaLinha
                paresSomaLinha = linha[i] + linha[i + 1]

    for c in range(0, numeroMatriz):
        for l in range(0, numeroMatriz - 1):
            somaColuna = int(linhas[l][c]) + int(linhas[l+1][c])
            if somaColuna > maiorSomaColuna:
               maiorSomaColuna = somaColuna
               paresSomaColuna = linhas[l][c] + linhas[l+1][c]

    for d in range(0, numeroMatriz - 1):
        somaDiagonal = int(linhas[d][d]) + int(linhas[d+1][d+1])
        if somaDiagonal > maiorSomaDiagonal:
            maiorSomaDiagonal = somaDiagonal
            paresSomaDiagonal = linhas[d][d] + linhas[d+1][d+1]

    print(f'Falei que era fácil Dustinzinho...\n'
          f'Pegando todas os números que formam as combinações dos pares de cada sentido temos...\n'
          f'Password: {paresSomaLinha}{paresSomaColuna}{paresSomaDiagonal}')