# Crie abstração para uma super classe Funcionario com duas subclasses. Imprima todos os dados.

class Funcionarios:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.__cpf = None
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu__cpf):
        self.__cpf = meu__cpf
    
class Professor(Funcionarios):
    def __init__(self, nome, idade, salario, disciplina, cpf):
        super().__init__(nome, idade, salario)
        self.disciplina = disciplina
        self.cpf = super().set_cpf(cpf)
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Salario: {self.salario} R$, Disciplina: {self.disciplina}, CPF: {self.get_cpf()}'

class TecEnfermagem(Funcionarios):
    def __init__(self, nome, idade, salario, expecializacao, cpf):
        self.expecializacao = expecializacao
        super().__init__(nome, idade, salario)
        self.cpf = super().set_cpf(cpf)

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Salario: {self.salario} R$, Expecialização: {self.expecializacao}, CPF: {self.get_cpf()}'
         
funcionario = Professor('Jeferson', 19, 1320.00, 'Matematica', 123456789)
print(funcionario)
funcionario2 = TecEnfermagem('Jeferson', 19, 1320.00, 'Urgência e Emergência', 1234567890)
print(funcionario2)