
contador = 0
checkBazinga = False

while True:
    mensagem = str(input()).strip().lower()
    if mensagem == 'começou a trabalhar na caltech':
        contador = 1
        checkBazinga = False
    elif mensagem == 'bazinga':
        if not checkBazinga:
            contador -= 1
            checkBazinga = True
    elif mensagem == 'trabalho sobre a string theory':
        if contador == 1:
            contador += 1
            checkBazinga = False
    elif mensagem == 'ganhar o chancellor de ciência':
        if contador == 2:
            contador += 1
            checkBazinga = False
    elif mensagem == 'pensar na teoria de cooper-hofstader':
        if contador == 3:
            contador += 1
            checkBazinga = False
    elif mensagem == 'criou a super assimetria':
        if contador == 4:
            contador += 1
            checkBazinga = False
    elif mensagem == 'ganhar o nobel':
        if contador == 5:
            contador += 1
        break
    elif mensagem == 'tinha que ser o engenheiro sem phd do wolowitz' or mensagem == 'leonard seu anão covarde' or mensagem == 'tu é muito burro raj':
        print('Não xingue seus amigos Sheldon!')
        checkBazinga = True
    elif mensagem == 'é o fim da sstrada pra sheldon cooper':
        break
    else:
        checkBazinga = True


if contador == 0:
    print('Que potencial desperdiçado...')
elif contador == 1 or contador == 2:
    print('Tão perto, mas tão longe')
elif contador == 3 or contador == 4:
    print('Não desista Sheldon, você ainda têm muito para alcançar!')
elif contador == 5:
    print('Nãoooooo, esse momento ia ser seu Sheldon')
else:
    if contador == 6:
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
