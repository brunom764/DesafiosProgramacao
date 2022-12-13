Não é novidade que o Siri Cascudo é o melhor restaurante da Fenda do Bikini, mas ultimamente o movimento tem aumentado bastante e Lula Molusco e Bob Esponja, sozinhos, já não estão mais dando conta de anotar e preparar tantos pedidos, ficar de olho no estoque e pensar em novas adições para o cardápio.

O Sr. Sirigueijo sempre ligado em meios de como aumentar os lucros do seu negócio e a produtividade de seus funcionários, ficou sabendo de um tal de ERP, ou Enterprise Resource Planning, um sistema de informação que tem a função de integrar diversos setores de uma empresa como estoque, vendas e finanças para facilitar a gestão de um negócio e a tomada de decisões.

Diante disso, ele contratou você, jovem graduando do CIn, para desenvolver e implementar esse sistema para que ele possa manter um relatório do estoque, das vendas, da entrada e saída de dinheiro, além de saber quais receitas seriam boas adições ao cardápio de acordo com a demanda do público do Siri Cascudo.



Para ajudá-lo, aqui vão as informações que você vai precisar para desenvolver esse sistema:

As receitas oferecidas, a princípio, serão hamburguer de siri (siri, pao, alface, tomate, queijo, picles); pizza de siri (siri, trigo, fermento, ovos, queijo); siri frito (siri, manteiga) e siri a parmegiana (siri, trigo, ovos, queijo, tomate).
O caixa sempre inicia com 40 reais. Não se preocupe, não acontecerá do caixa ficar zerado.
Ao começar, teremos 5 unidades de todos os ingredientes e , caso um ingrediente for necessário para uma receita e ele tiver acabado, devemos comprar sempre de 4 em 4 unidades, usando o dinheiro disponível no caixa.
Para cada pedido, usamos 1 unidade de cada ingrediente na receita.
Todas as receitas adicionadas durante o programa deverão ser vendidas por um preço referente à soma dos valores da unidade de cada ingrediente necessário e mais 5 reais.
Abaixo segue uma tabela com os ingredientes que serão utilizados para as receitas e as opções de refeições oferecidas, juntamente com seus respectivos preços por unidade:
Obs.1: Para a resolução devem ser utilizadas ambas as estruturas de dados tuplas e dicionários e não será permitido o uso de listas. Apenas será permitido o uso da função split para separar os ingredientes da entrada e os transformar em uma tupla.

Obs.2: O nome das comidas sempre vão aparecer na forma em que foram escritas acima.

Input

A entrada, inicialmente, terá um número indeterminado de pedidos, seguindo o exemplo abaixo:

pedido_1

pedido_2

…

pedido_n

O segundo tipo de entrada ocorre caso uma comida que não esteja no cardápio seja requisitada mais de duas vezes. Nesse momento, para que o novo pedido possa ser adicionado ao cardápio, você receberá um input com todos os ingredientes necessários para o seu preparo separados por um espaço como a seguir:

ingrediente_1 ingrediente_2 ... ingrediente_n

Obs.3: Use try/except com EOFError para pegar todas as entradas.

Obs.4: Para o preparo dos novos pedidos, serão utilizados apenas ingredientes previamente mencionados na tabela de preços.

Output

A cada pedido entregue pelo Bob Esponja deverá ser printado:

"{pedido} saindo..."

Ou se a comida não estiver no cardápio:

"{pedido} ainda não é uma opção disponível."

Logo após adicionarmos uma nova opção ao cardápio, a saída será:

"Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo."

Quando não houverem mais entradas, primeiro printaremos:

"##### Fim do expediente #####"

Em seguida, o programa deve exibir o valor arrecadado com as vendas, sem considerar os 40 reais iniciais:

"O lucro obtido no dia de hoje foi de R${total}."

E por último, caso hambúrguer de siri tenha sido o pedido mais vendido:

"O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!"

Caso outro pedido qualquer tenha sido o mais vendido:

"{mais_vendido} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri."

Em que {pedido} corresponde a um pedido realizado por algum cliente, {mais_vendido} o pedido que mais saiu e deverá ser printado com a primeira letra maiúscula e {total} um valor inteiro referente ao lucro das vendas.

Examples

Case: 1

Input

hamburguer de siri
hamburguer de siri
siri frito
hamburguer de siri
pizza de siri
siri frito

Output

hamburguer de siri saindo...
hamburguer de siri saindo...
siri frito saindo...
hamburguer de siri saindo...
pizza de siri saindo...
siri frito saindo...
##### Fim do expediente #####
O lucro obtido no dia de hoje foi de R$112.
O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!

Case: 2

Input

siri com fritas
siri frito
siri com fritas
siri com fritas
siri batata queijo
siri frito
siri com fritas

Output

siri com fritas ainda não é uma opção disponível.
siri frito saindo...
siri com fritas ainda não é uma opção disponível.
Atendendo demandas, siri com fritas é a mais nova adição ao cardápio do Siri Cascudo.
siri frito saindo...
siri com fritas saindo...
##### Fim do expediente #####
O lucro obtido no dia de hoje foi de R$52.
Siri frito está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário hambúrguer de siri.