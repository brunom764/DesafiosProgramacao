Você, Mestre dos Magos, presenciou 6 jovens entrarem na sua terra mágica e tornou eles heróis, equipados com Armas do Poder cedidas por você e os embarcou em muitas aventuras por sua terra, combatendo vilões e ajudando eles a voltarem para casa. Após muitas tribulações, chegou a hora do último desafio, em uma épica luta que vai ser eternizada em lenda e canto por todo o Reino.

A party com o Mestre dos Magos

Nessa luta final, todos vocês se juntaram para que eles possam voltar para o mundo deles. Cada membro do grupo tem forças e fraquezas diferentes, e todos tem a oportunidade de lutar. Se conseguirem derrotar seu inimigo, estarão livres, mas precisam ser rápidos, pois a cada turno ele fica mais perto de derrotá-los.

Cada membro do grupo é dotado de arma e armadura. A arma determina o quanto de dano é infligido, e a armadura o quão mais rápido o grupo é derrotado. A luta se dá em turnos, e a cada turno um de vocês tem a oportunidade de atacar, executando dano no adversário. Após isso, o progresso do adversário em derrotar o grupo aumenta, ou seja, a quantidade de turnos restantes na batalha diminuem, a depender do quão desprotegido estava quem atacou o adversário. Se os pontos de vida do vilão acabarem quando os heróis estiverem prestes a serem derrotados, os heróis ainda vencem. Caso o Mestre dos Magos ataque, o combate é determinado como vitória do grupo instantaneamente.

Grupo: (arma / armadura)

Bobby: grande espada / armadura media

Diana: dardo / armadura leve

Eric: grande espada / armadura pesada

Hank: espada / armadura media

Presto: cajado / armadura leve

Sheila: espada / armadura leve

Uni: chifre / armadura leve

Armas:

Chifre: 2 de dano

Cajado: 4 de dano

Espada: 6 de dano

Grande espada: 8 de dano

Dardo: 12 de dano

Armaduras:

Armadura pesada: não aumenta o progresso do adversário

Armadura media: aumenta em 1 o progresso do adversário

Armadura leve: aumenta em 3 o progresso do adversário

Nota: além e independente da armadura, a cada ataque a batalha fica um turno mais próxima de ser perdida

Input

Uma linha contendo o nome do adversário

Adversario

Existem alguns adversários conhecidos, nesses casos, os pontos de vida serão:

Vingador: 30

Tiamat: 20

Vingador das Sombras: 14
Caso o adversário não seja um desses, o número de pontos de vida é 9.

Uma linha contendo em quantos turnos o grupo será derrotado

Turnos

Para cada turno até o desfecho da luta:

Uma linha contendo o nome de quem atacou naquele turno

Personagem

Output

Caso os pontos de vida do adversário sejam reduzidos a 0 ou menos durante a batalha:

"{personagem} executou o ultimo golpe em {adversario}, estamos livres!"

Onde {personagem} foi o ultimo personagem a atacar

Caso os pontos de vida sejam maiores que 0 ao final dos turnos:

"Oh nao, {adversario} e muito forte, este e o fim!"

Caso o Mestre dos Magos intervenha e ataque:

"Muito obrigado amigo, que nos vejamos novamente um dia"

Examples

Case: 1

Input

Vingador
8
Bobby
Diana
Eric
Presto

Output

Presto executou o ultimo golpe em Vingador, estamos livres!

Case: 2

Input

2033 goblins
5
Uni
Eric

Output

Eric executou o ultimo golpe em 2033 goblins, estamos livres!

Case: 3

Input

Tiamat
12
Hank
Sheila
Mestre dos Magos

Output

Muito obrigado amigo, que nos vejamos novamente um dia

Case: 4

Input

Demonio das Sombras
1
Eric

Output

Oh nao, Demonio das Sombras e muito forte, este e o fim!