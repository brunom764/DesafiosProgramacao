adversario = input()
turnos = int(input())
dicionario = {}
listaInfo = []

grupo = ['Bobby', 'Diana', 'Eric', 'Hank', 'Presto', 'Sheila', 'Uni']
arma = ['grande espada', 'dardo', 'grande espada', 'espada', 'cajado', 'espada', 'chifre']
dano = [8, 12, 8, 6, 4, 6, 2]
armadura = ['armadura media', 'armadura leve', ' armadura pesada', 'armadura media', 'armadura leve', 'armadura leve', 'armadura leve']

for i in range(len(grupo)):
    dicionario['personagem'] = grupo[i]
    dicionario['arma'] = arma[i]
    dicionario['dano'] = dano[i]
    dicionario['armadura'] = armadura[i]
    listaInfo.append(dicionario.copy())

listaAdvesarios = [{'nome': 'Vingador', 'vida': 30}, {'nome': 'Tiamat', 'vida': 20}, {'nome': 'Vingador das Sombras', 'vida': 14}]

if adversario == 'Vingador':
    vida = 30
elif adversario == 'Tiamat':
    vida = 20
elif adversario == 'Vingador das Sombras':
    vida = 14
else:
    vida = 9


while turnos != 0 and vida > 0:
    try:
        atacou = input()
    except EOFError:
        break
    if atacou == 'Mestre dos Magos':
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
        vida = 0
    else:
        damage = 0
        armad = ''
        for person in listaInfo:
            if person['personagem'] == atacou:
                damage = person['dano']
                armad = person['armadura']
        if armad == 'Armadura media':
            turnos -= 1
        if armad == 'Armadura leve':
            turnos -= 3
        vida = vida - int(damage)
        if vida < 1:
            print(f'{atacou} executou o ultimo golpe em {adversario}, estamos livres!')
    turnos -= 1

if vida > 0:
    print(f'Oh nao, {adversario} e muito forte, este e o fim!')