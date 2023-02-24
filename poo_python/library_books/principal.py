from poo_python.library_books.biblioteca import Biblioteca
from poo_python.library_books.livro import Livro


biblioteca = Biblioteca()

livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 97)
livro2 = Livro(" Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

biblioteca.mostrar_livros()
