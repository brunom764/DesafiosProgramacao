# Você foi contratado pela Balão NET para desenvolver um sistema de histórico de pesquisas em seu mais novo navegador,
# o "balão_explorer”. Para isso foi requisitada a utilização de uma lista duplamente encadeada para armazenar
# as pesquisas e também 4 funcionalidades básicas do sistema: busca, remoção, adição e exibição do histórico.
#
# Input
#
# O programa receberá uma quantidade indefinida de entradas e deverá encerrar quando o comando final “END” for dado . Comandos :
# ADD X (X poderá ser qualquer string)
# REM X (X poderá ser qualquer string)
# EXIB
# FIND X (X poderá ser qualquer string , desde que contida na lista)
# END
#
# o comando ADD deverá inserir o elemento na sua lista duplamente encadeada
#
# o comando REM deverá remover o elemento na sua lista duplamente encadeada
#
# o comando EXIB deverá printar todo o histórico contido na lista
#
# o comando FIND deverá localizar um elemento já existente na lista e colocá-lo na primeira posição dela
#




class No:
    def __init__(self, data):
        self.data = data  # valor
        self.prev = None  # -1
        self.next = None  # +1


class listaDuplaEncad:
    def __init__(self):
        self.head = None  # primeiro nó
        self.tail = None  # ultimo nó

    def pedido(self, comando, entrada): #Chama todos os metodos abaixo
        if comando == "ADD":
            self.add(entrada[1])

        elif comando == "REM":
            self.rem(entrada[1])

        elif comando == "EXIB":
            self.exib()

        elif comando == "FIND":
            self.find(entrada[1])

        elif comando == "END":
            return True
        return False

    def add(self, site):
        novoSite = No(site)  # cria nó

        if self.tail is None:
            self.head = self.tail = novoSite  # primeiro nó
        else:  # add um novo nó no final da lista
            novoSite.prev = self.tail
            self.tail.next = novoSite
            self.tail = novoSite

    def rem(self, site):
        siteAnalisado = self.head
        while siteAnalisado is not None:
            if siteAnalisado.data == site:
                if siteAnalisado.prev is not None:
                    siteAnalisado.prev.next = siteAnalisado.next  #o next do nó anterior deve ser apontado pro next do nó remov
                else:
                    self.head = siteAnalisado.next

                if siteAnalisado.next is not None:
                    siteAnalisado.next.prev = siteAnalisado.prev
                else:
                    self.tail = siteAnalisado.prev
                return
            siteAnalisado = siteAnalisado.next

    def find(self, site):
        siteAnalisado = self.head
        presente = False
        while siteAnalisado is not None:
            if siteAnalisado.data == site:
                presente = True
                break
            siteAnalisado = siteAnalisado.next
        if presente:
            self.rem(site)
            self.add(site)  # add no head


    def exib(self):
        siteAnalisado = self.tail
        while siteAnalisado is not None:  # printa tds os sites ate ser none
            print(siteAnalisado.data)
            siteAnalisado = siteAnalisado.prev


# parte principal
sites = listaDuplaEncad()
end = False

while not end:
    entrada = input().split()
    end = sites.pedido(entrada[0], entrada)
