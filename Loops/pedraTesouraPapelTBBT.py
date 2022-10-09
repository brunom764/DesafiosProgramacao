rodadas = int(input())
contadorSheldon = 0
contadorRaj = 0

for i in range(0, rodadas):
    escolhaSheldon = str(input()).lower().strip()
    escolhaRaj = str(input()).lower().strip()

    if escolhaSheldon == 'lagarto' and escolhaRaj == 'spock':
        contadorSheldon += 1
    elif escolhaRaj == 'lagarto' and escolhaSheldon == 'spock':
        contadorRaj += 1

    elif escolhaSheldon == 'tesoura' and escolhaRaj == 'lagarto':
        contadorSheldon += 1
    elif escolhaRaj == 'tesoura' and escolhaSheldon == 'lagarto':
        contadorRaj += 1

    elif escolhaSheldon == 'spock' and escolhaRaj == 'tesoura':
        contadorSheldon += 1
    elif escolhaRaj == 'spock' and escolhaSheldon == 'tesoura':
        contadorRaj += 1

    elif escolhaSheldon == escolhaRaj:
        pass
    else:
        pass

if contadorSheldon > contadorRaj:
    print("BAZINGA! EU SOU O SENHOR DA SALA!")
elif contadorRaj > contadorSheldon:
    print("ENGOLE ESSA, SHELDON!")
else:
    print("Oh não, precisamos de outra rodada.")