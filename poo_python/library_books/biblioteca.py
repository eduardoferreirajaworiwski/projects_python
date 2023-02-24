from poo_python.library_books.livro import Livro


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def mostrar_livros(self):
        for livro in self.livros:
            livro.mostrar_informacoes()
