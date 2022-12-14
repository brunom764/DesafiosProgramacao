Jiro Horikoshi, engenheiro de aviões, gasta grande parte do seu tempo trabalhando com cálculos matemáticos, e muitos desses cálculos são operações envolvendo matrizes. Em busca de diminuir a quantidade de cálculos que ele precisa fazer à mão e salvar tempo para que ele trabalhe em outras áreas, assim como reduzir possíveis erros de calculo, Jiro quer sua ajuda para construir um programa de uma calculadora de matrizes, tendo as operações de soma, subtração e multiplicação de matrizes assim como multiplicação de uma matriz por um escalar. A sua calculadora precisa funcionar apenas com matrizes quadradas e mesmo tamanho.

Input

A primeira linha de entrada é um inteiro que determina o tamanho das duas matrizes que vão ser usadas no programa

N

Em seguida, você vai receber a matriz quadrada de tamanho N m1, separadas por espaços

m1_00 m1_01 . . . m1_0N
m1_10 m1_11 . . . m1_1N
. . .
m1_N0 m1_N1 . . . m1_NN

Depois, você vai receber a matriz quadrada de tamanho N m2, no mesmo formato

m2_00 m2_01 . . . m2_0N
m2_10 m2_11 . . . m2_1N
. . .
m2_N0 m2_N1 . . . m2_NN

Após isso, você vai receber um inteiro representando a quantidade de operações que vão ser realizadas nas matrizes.

qtd_op

Em seguida, você vai receber qtd_op operações, se a operação for soma, subtração ou produto de matrizes (representadas por +, - e . respectivamente):

mr = ma op mb

onde mr (pode ter valor ‘m1’ ou ‘m2’) é a matriz que vai receber o resultado, ma e mb (pode ter valor ‘m1’ ou ‘m2’, podem ser matrizes diferentes ou iguais) são as matrizes que vão ser usadas na operação.

Já se for uma multiplicação por escalar:

mr = m * k

ou

mr = k * m

onde k é o escalar (sempre um inteiro)

Output

A saída consiste em imprimir o resultado da última operação realizada, linha por linha e separando os valores com espaços:

mr_00 mr_01 . . . mr_0N
mr_10 mr_11 . . . mr_1N
. . .
mr_N0 mr_N1 . . . mr_NN

Examples

Case: 1

Input

3
31 21 46
37 9 8
37 29 2
10 12 40
8 11 8
26 22 11
2
m1 = m2 + m2
m2 = m1 - m2

Output

10 12 40
8 11 8
26 22 11

Case: 2

Input

3
2 6 2
5 2 5
4 9 1
8 6 8
3 7 7
6 2 8
4
m2 = m1 + m2
m2 = m1 * 2
m1 = 3 * m2
m2 = m1 . m2

Output

504 504 432
480 948 300
684 612 648