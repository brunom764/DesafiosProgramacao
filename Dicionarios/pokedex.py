pokedex = []
listaDesc = []
pokemon = {}
comando = []
listPokemon = []
continua = True

while continua:
    tem = False
    try:
        infoComando = input()
        comando = infoComando.split(' ')

        if len(listPokemon) == 0:
            if comando[0] == 'ADD':
                desc = str(input())
                listaDesc.append(desc)
                listPokemon.append(comando[1])
                pokemon['pokemon'] = comando[1]
                pokemon['DESC'] = desc
                pokedex.append(pokemon.copy())
                print('Pokémon adicionado com sucesso')
            else:
                print('Ainda não há registro desse Pokémon')
        else:
            try:
                for i in range(0, len(listPokemon)):
                    if listPokemon[i] == comando[1]:
                        tem = True
                    else:
                        pass
            except IndexError:
                pass

            if comando[0] == 'ADD' and not tem:
                desc = str(input())
                listaDesc.append(desc)
                listPokemon.append(comando[1])
                pokemon['pokemon'] = comando[1]
                pokemon['DESC'] = desc
                pokedex.append(pokemon.copy())
                print('Pokémon adicionado com sucesso')
                #print(pokedex)
            elif comando[0] == 'ADD' and tem:
                print('Pokémon já adicionado na Pokédex')
            elif comando[0] == 'DESC':
                if tem:
                    for i in range(0, len(listPokemon)):
                        if listPokemon[i] == comando[1]:
                            print(listaDesc[i])
                else:
                    print('Ainda não há registro desse Pokémon')

    except EOFError:
        continua = False