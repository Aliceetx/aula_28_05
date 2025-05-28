class livro:
    def __init__(self, titulo_inicial=0):
        self._titulo = titulo_inicial

    def definir_titulo(self, novo_titulo):
        self._titulo = novo_titulo  

    def mostrar_titulo(self):
        return self._titulo

livro1 = livro ("Mil Beijos de Garoto")
livro1.definir_titulo ("Mil Beijos de Garoto")
print (livro1.mostrar_titulo())

livro2 = livro ("2016")
print(livro2.mostrar_titulo())
