class Livro:
    def __init__(self, titulo, autor, ano_publicacao, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.quantidade_paginas = quantidade_paginas

    def mostrar_informacoes(self):
        print("Título: ", self.titulo)
        print("Autor: ", self.autor)
        print("Ano de publicação: ", self.ano_publicacao)
        print("Quantidade de páginas: ", self.quantidade_paginas)
