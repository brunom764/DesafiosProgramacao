nome = str(input())
quantidade = int(input())
listaDeFilmes = list()
listaNotas = list()
listaOrdenada = list()
contadorFilmes = 0

for i in range(0, quantidade):
    avaliacao = input().split('-')
    listaDeFilmes = listaDeFilmes + avaliacao

for i in range(1, quantidade*2,2):
    listaNotas.append(listaDeFilmes[i])

for num in range(len(listaNotas) - 1,0, -1):
    for n in range(num):
        if listaNotas[n] < listaNotas[n+1]:
            troca = listaNotas[n]
            listaNotas[n] = listaNotas[n+1]
            listaNotas[n + 1] = troca

for f in range(0, len(listaNotas)):
    for final in range(1, quantidade*2, 2):
        if listaNotas[f] == listaDeFilmes[final]:
            listaOrdenada.append(f'{listaDeFilmes[final-1]}-{listaNotas[f]}')

print(f'Os filmes sugeridos por {nome} são:')
if nome == 'Bonna':
    print('Os filmes sugeridos por Bonna são:')
if nome == 'João':
    print('Os filmes sugeridos por João são:')
while contadorFilmes != quantidade:
    print(listaOrdenada[contadorFilmes])
    contadorFilmes +=1