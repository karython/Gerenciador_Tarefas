class Projeto:
    def __init__(self, nome, descricao, funcionarios):
        self.__nome = nome
        self.__descricao = descricao
        self.__funcionarios = funcionarios


    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def funcionarios(self):
        return self.__funcionarios

    @funcionarios.setter
    def funcionarios(self, funcionarios):
        self.__funcionarios = funcionarios