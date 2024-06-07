class Funcionario:
    def __init__(self, nome, dtNascimento, cpf):
        self.__nome = nome
        self.__dtNascimento = dtNascimento
        self.__cpf = cpf


    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def dtNascimento(self):
        return self.__dtNascimento

    @dtNascimento.setter
    def dtNascimento(self, dtNascimento):
        self.__dtNascimento = dtNascimento

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf


