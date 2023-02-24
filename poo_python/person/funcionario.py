from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        super().apresentar()
        print(f"Eu sou um(a) {self.cargo} e ganho R${self.salario} por mês.")
