from ..models import funcionario_model
from api import db

'''
    esse modulo de serviço fica responsavel por adicionar uma nova funcionario no banco de dados
    usando o sqlalchemy, usando o add e o commit para fazer o salvamento de dados e retorna a funcionario
'''

# metodo para cadastrar uma nova funcionario
def cadastrar_funcionario(funcionario):
    funcionario_bd = funcionario_model.Funcionario(nome=funcionario.nome, dtNascimento=funcionario.dtNascimento,
                                    cpf=funcionario.cpf)

    db.session.add(funcionario_bd)
    db.session.commit()
    return funcionario_bd


# metodo para listar todos os funcionarios
def listar_funcionarios():
    funcionarios = funcionario_model.Funcionario.query.all()
    return funcionarios

# metodo para editar um funcionario partir do seu ID
def editar_funcionario(funcionario_bd, funcionario_novo):
    funcionario_bd.nome = funcionario_novo.nome
    funcionario_bd.dtNascimento = funcionario_novo.dtNascimento
    funcionario_bd.cpf = funcionario_novo.cpf
    db.session.commit()


# metodo para excluir uma funcionario a partir do seu ID
def excluir_funcionario(funcionario):
    db.session.delete(funcionario)
    db.session.commit()


# metodo para listar uma funcionario pelo seu ID
def listar_funcionario_id(id):
    funcionario = funcionario_model.Funcionario.query.filter_by(id=id).first() #aplicando a query com filtro
    return funcionario