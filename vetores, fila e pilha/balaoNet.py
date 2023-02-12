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
# exemplo :
#
# lista = d - b - c - a
#
# FIND(“a”)
#
# EXIB
#
# resultado da lista = a - d - b - c
#
# Output
#
# Após o comando EXIB será imprimido o histórico, exemplo:
#
# site1.com.br
#
# site2.com.br



class BalaoExplorer:
    def __init__(self):
        self.lista = list()
        self.end = False


    def checkEnd(self):
        return self.end

    def caminho(self, comando):
        if comando[0:3] == "ADD":
            site = comando[4:]
            self.lista.insert(0, site)

        elif comando[0:3] == "REM":
            site = comando[4:]
            if site in self.lista:
                self.lista.remove(site)

        elif comando[0:4] == "FIND":
            site = comando[5:]
            for s in self.lista:
                if s == site:
                    self.lista.remove(site)
                    self.lista.insert(0, site)

        elif comando[0:3] == "EXI":
            if len(self.lista) > 0:
                for i in range(len(self.lista)):
                    print(self.lista[i].strip())

        elif comando[0:3] == "END":
            self.end = True

        else:
            pass



end = False
lista = BalaoExplorer()
while not end:
    com = input()
    lista.caminho(com)
    end = lista.checkEnd()


