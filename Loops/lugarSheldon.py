
temperatura = 30
fome = True
internet = 0
internetBoa = True
temperaturaBoa = False

while True:
    comando = str(input()).strip().lower()
    if comando == 'parar':
        break
    if comando == 'ir para o grad':
        temperatura -= 5
        internet += 300
    elif comando == 'sair para a rua':
        temperatura += 5
    elif comando == 'comer uma quentinha':
        fome = False
    elif comando == 'conectar no wifi':
        internet += 100
    else:
        print('Entrada inválida')

if temperatura >= 30:
    print('A temperatura aqui não está agradável')
else:
    print('Agora sim, está aconchegante')
    temperaturaBoa = True

if fome == True:
    print('Meu corpo precisa de comida')

if internet < 100:
    print('Essa conexão está horrível')
    internetBoa = False

if fome == False and internetBoa == True and temperaturaBoa == True:
    print('Finalmente um lugar preciso para mim!')