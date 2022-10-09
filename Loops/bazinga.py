
piadaBoa = 0
piadaRuim = 0
contador = 0

while True:
    piada = str(input()).strip()
    if piada == 'Fim do Show!':
        break
    else:
        reacao = str(input()).strip()
        contador += 1
        if reacao != 'BAZINGA!':
            piadaRuim += 1
        else:
            piadaBoa += 1


if piadaBoa / contador > 0.6:
    print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif piadaRuim / contador > 0.6:
    print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
    print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
