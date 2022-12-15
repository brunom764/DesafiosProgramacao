# Faça um sistema de compras:
# a. Crie uma classe abstrata Empreendimento que possui os métodos
# abstratos getNome, setNome, getCNPJ, setCNPJ, getEndereco,
# setEndereco, getLucro, setVenda.
# b. Crie uma subclasse Supermercado que herda da classe
# Empreedimento e implementa os métodos __init__, getNome,
# setNome, getCNPJ, setCNPJ, getSaldo, setVenda. Ao inicializar um
# objeto dessa classe, deve-se passar o nome, CNPJ e endereço como
# parâmetros.
# c. O método getSaldo retorna o valor do atributo encapsulado saldo. O
# método setVenda atualiza o valor do atributo encapsulado saldo
# somando-o com um atributo fornecido como parâmetro.
# d. Inicialize 3 objetos do tipo Supermercado: VarejaoCIn, CompraUFPE e
# EstudantesVarzea. Peça para o usuário fornecer as informações
# iniciais e depois pergunte se houve alguma venda para cada um dos
# supermercados. Encerre imprimindo as informações gerais dos
# supermercados.

class Emprendimento:
    def __init__(self, initNome, initCNPJ, initEndereco):
        self.nome = initNome
        self.cnpj = initCNPJ
        self. enederco = initEndereco
        self.lucro = 0
        self.venda = 0

    def getNome(self):
        return self.nome
    def setNome(self,nomeNew):
         self.nome = nomeNew
    def getCNPJ(self):
        return self.cnpj
    def getEndereco(self):
        return self.enederco
    def setEndereco(self, enderecoNew):
        self.endereco = enderecoNew
    def getLucro(self):
        pass
    def setVenda(self, vendaNew):
        pass

class Supermercado(Emprendimento):

    def __init__(self,initNome, initCNPJ, initEndereco):
        super().__init__(initNome, initCNPJ, initEndereco)
        self.saldo = 0
    def getNome(self):
        return self.nome
    def setNome(self,nomeNew):
         self.nome = nomeNew
    def getCNPJ(self):
        return self.cnpj
    def setCNPJ(self, cnpjNew):
        self.cnpj = cnpjNew
    def getSaldo(self):
        return self.saldo
    def setVenda(self, vendaNew):
        self.saldo += int(vendaNew)


varejaoCIn = Supermercado('Varejao CIn',123456, 'CIn')
varejaoCIn.setVenda(10)
compraUFPE = Supermercado('Compra UFPE',123465, 'UFPE')
compraUFPE.setVenda(100)
estudantesVarzea = Supermercado('Estudantes Varzea',123457, 'Varzea')
estudantesVarzea.setVenda(150)
#print(estudantesVarzea.getNome())

