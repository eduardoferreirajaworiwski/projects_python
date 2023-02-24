from pessoa import Pessoa
from funcionario import Funcionario

# Lista para armazenar os objetos Pessoa
pessoas = []

# Loop para cadastrar pessoas
while True:
    nome = input("Digite o nome da pessoa (ou digite 'fim' para encerrar): ")
    if nome == "fim":
        break
    idade = int(input("Digite a idade da pessoa: "))
    p = Pessoa(nome, idade)
    pessoas.append(p)
    p.apresentar()

# Loop para cadastrar funcionários
while True:
    nome = input(
        "Digite o nome do funcionário (ou digite 'fim' para encerrar): ")
    if nome == "fim":
        break
    idade = int(input("Digite a idade do funcionário: "))
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    f = Funcionario(nome, idade, cargo, salario)
    f.apresentar()
