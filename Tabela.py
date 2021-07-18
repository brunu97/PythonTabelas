tabela = [["Nomes", "Valores", "Adicional"], ["Nome A", 50, 80], ["Nome B", 80], ["Nome C", 150]]


class Tabela:
    def __init__(self, lista, modo):
        self.lista = lista
        self.extra_spc = 6
        if modo not in [0, 1, 2, 3] or modo is None: # Modo de desenho da coluna/linha principal
            # 0 - Sem, 1 - Esquerda, 2 - Topo, 3 - Ambos
            self.modo = 0
        else:
            self.modo = modo
        self.lim = ""

    def desenhaTabela(self):
        lista = list([str(s) for s in e] for e in self.lista)
        colunas_comprimento = []
        
        cmp = len(lista[0]) # Verifica qual é a coluna dos nomes para obter o comprimento ou altura da tabela

        for j in range(cmp):  # Obtem o maior elemento de cada coluna
            c = 0
            for i in range(len(lista)):
                
                # Caso a Linha não tiver elemento adiciona um vazio
                try: 
                    len(lista[i][j])
                except:
                    lista[i].append("-")

                if len(lista[i][j]) > c: c = len(lista[i][j])
            colunas_comprimento.append(c + self.extra_spc)

        for x, linha in enumerate(lista): # Desenha elementos
            n = 0
            try:
                for i, e in enumerate(linha):
                    n += len("| " + e + " " * (colunas_comprimento[i] - len(e)))
                    if self.modo in [1, 3]:
                        self.lim = "| " if i == 0 else ""
                    print(e + " " * (colunas_comprimento[i] - len(e)), end=self.lim)
            except IndexError:
                raise IndexError("Comprimento da linha não é formatável nesta tabela.")
            print("")
            if self.modo in [2, 3]:
                if x == 0: print("-" * (n + 1))


t = Tabela(tabela, 2)
t.desenhaTabela()
