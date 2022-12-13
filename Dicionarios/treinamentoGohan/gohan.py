dicionario = {}
comparaLista = []
pedras = int(input())
listaGohan = input().split(' ')
listaPicolo = input().split(' ')
igual = 0

for i in range(pedras):
    dicionario['gohan'] = listaGohan[i]
    dicionario['picolo'] = listaPicolo[i]
    comparaLista.append(dicionario.copy())

#print(comparaLista)

for pedra in comparaLista:
    if pedra['gohan'] in listaPicolo:
        igual += 1
        listaPicolo.remove(pedra['gohan'])
       # print(listaPicolo)

if igual == pedras:
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')