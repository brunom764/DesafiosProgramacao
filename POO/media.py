# Faça um sistema de notas da sua sala:
# a. Crie uma classe Aluno que possui 3 notas. Ao inicializar a
# classe, passe como parâmetro o CPF e o nome do aluno.
# b. A classe possui 3 métodos: inicializarNota(nota,
# numeroProva) que tem como atributos a nota e o número
# (1,2,3) da nota a ser inicializada; verificaSituacaoMedia(),
# que não possui atributos e retorna True se o aluno tem
# média acima de 7 e False caso contrário. Se as 3 notas não
# foram inicializadas, imprima uma mensagem na tela e
# retorne False; imprimeInformacoes(), que não possui
# atributos e imprime o nome, CPF e as 3 notas do aluno. Se
# alguma das notas não foi fornecida, imprima "nota x não
# fornecida".

class NotaAluno:
    def __init__(self,__initCpf__, __initNome__):
        self._cpf = __initCpf__
        self._nome = __initNome__
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0

    def inicializarNota(self, nota, numProva):
        if numProva == 1:
            self.nota1 = nota
        elif numProva == 2:
            self.nota2 = nota
        else:
            self.nota3 = nota

    def verificaSituacaoMedia(self):
        if self.nota1 or self.nota2 or self.nota3 == 0:
            print('Falta inicializar as notas')
        else:
            media = (self.nota1 + self.nota2 + self.nota3)/3
            if media >= 7:
                return True
            else:
                return False

    def imprimeInfo(self):
        print(self._nome, self._cpf, self.nota1, self.nota2,self.nota3)



aluno1 = NotaAluno(1111111111, 'bruno')
aluno1.inicializarNota(9,1)
aluno1.inicializarNota(8,2)
aluno1.inicializarNota(8,3)
aluno1.imprimeInfo()