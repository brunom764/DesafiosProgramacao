class Fila:
    def __init__(self):
        self.fila1 = []
        self.fila2 = []
        self.caixa1 = 0
        self.caixa2 = 0

    def mudaFila(self, filaVazia, filaCheia):
        if len(filaCheia) % 2 != 0: # impar
            metade = (len(filaCheia) + 1) // 2
        else:
            metade = len(filaCheia) // 2

        filaVazia = filaCheia[metade:][::-1] # metade ao contrario
        filaCheia = filaCheia[:metade] # fica metade

        return filaVazia, filaCheia

    def enfileirar(self, nome, caixa, valor):
        if caixa == 1:
            self.fila1.append((nome, valor))
            print(f"{nome} entrou na fila 1")
        elif caixa == 2:
            self.fila2.append((nome, valor))
            print(f"{nome} entrou na fila 2")

    def filaAndou(self, caixa):
        if caixa == 1:
            if len(self.fila1) == 0:
                self.fila1, self.fila2 = self.mudaFila(self.fila1, self.fila2)
            proximo = self.fila1.pop(0) # pega o primeiro elemento e remove
            print(f"{proximo[0]} foi chamado para o caixa {caixa}")
            self.caixa1 += proximo[1]

        elif caixa == 2:
            if len(self.fila2) == 0:
                self.fila2, self.fila1 = self.mudaFila(self.fila2, self.fila1)
            proximo = self.fila2.pop(0)
            print(f"{proximo[0]} foi chamado para o caixa {caixa}")
            self.caixa2 += proximo[1]


    def exibirCaixas(self):
        print(f"Caixa 1: R$ {self.caixa1:.2f}, Caixa 2: R$ {self.caixa2:.2f}")


fila = Fila()
end = False
while not end:
    entrada = input().split()
    comando = entrada[0]

    if comando == "ENTROU:":
        nome = entrada[1]
        caixa = int(entrada[2])
        valor = float(entrada[3])
        fila.enfileirar(nome, caixa, valor)

    elif comando == "PROXIMO:":
        caixa = int(entrada[1])
        if len(fila.fila1) == 0 and len(fila.fila2) == 0: # evitar runtime error
            end = True
        elif len(fila.fila1) + len(fila.fila2) == 1:
            if caixa == 1 and len(fila.fila1) == 0:
                fila.fila1.append(fila.fila2[0])
                fila.filaAndou(caixa)
            elif caixa == 2 and len(fila.fila2) == 0:
                fila.fila2.append(fila.fila1[0])
                fila.filaAndou(caixa)
            else:
                fila.filaAndou(caixa)
        else:
            fila.filaAndou(caixa)

    elif comando == "FIM":
        fila.exibirCaixas()
        end = True



