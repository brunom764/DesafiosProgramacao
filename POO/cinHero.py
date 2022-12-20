# A ONG CIn-Hero é uma instituição que salva animais perdidos pela cidade do Recife e divulga os bichinhos encontrados na internet.
# Você receberá inputs de 1 a 5 onde cada número corresponde/realiza um comando dentro do sistema do CIn-Hero.
# 1 - Cadastrar               
# 2 - Imprimir relatório            
# 3 - Imprimir os animais depois de uma data
# 4 - Remover um animal                        
# 5 - Finaliza o código


class Animal:
    def __init__(self):
        self.listaAnimais = []

    def cadastro(self,local, raca, data):
        self.listaAnimais.append([local, raca, data])

    def imprimeRelatorio(self):
        for animal in self.listaAnimais:
            print(f"Local: {animal[0]}\nRaça: {animal[1]}\nData: {animal[2]}\n")

    def dataInteresse(self,data:0):
        diaI, mesI, anoI = data.split("/")

        for animal in self.listaAnimais:
            dia, mes, ano = animal[2].split("/")

            if int(ano) > int(anoI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

            elif int(ano) == int(anoI) and int(mes) > int(mesI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

            elif int(ano) == int(anoI) and int(mes) == int(mesI) and int(dia) > int(diaI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

    def removerAnimal(self,raca, data):
        for animal in self.listaAnimais:
            if animal[1] == raca and animal[2] == data:
                local = animal[0]
                self.listaAnimais.remove([local,raca,data])



sistema = Animal()

while True:
    entrada = input()

    if entrada == "1":
        registros = input().split()
        sistema.cadastro(registros[0], registros[1], registros[2])

    elif entrada == "2":
        sistema.imprimeRelatorio()

    elif entrada == "3":
        dataBusca = input()
        sistema.dataInteresse(dataBusca)

    elif entrada == "4":
        remover = input().split()
        sistema.removerAnimal(remover[0], remover[1])

    elif entrada == "5":
        break
