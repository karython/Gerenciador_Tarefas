from ..models import projeto_model
from api import db
from ..services.funcionario_service import listar_funcionario_id
'''
    esse modulo de serviço fica responsavel por adicionar uma nova projeto no banco de dados
    usando o sqlalchemy, usando o add e o commit para fazer o salvamento de dados e retorna a projeto
'''

# metodo para cadastrar uma nova projeto
def cadastrar_projeto(projeto):
    projeto_bd = projeto_model.Projeto(nome=projeto.nome, descricao=projeto.descricao)

    # verifica os id dos funcionarios para adicionar no projeto
    for i in projeto.funcionarios:
        funcionario = listar_funcionario_id(i)
        projeto_bd.funcionarios.append(funcionario)

    db.session.add(projeto_bd)
    db.session.commit()
    return projeto_bd


# metodo para listar todas as projetos
def listar_projeto():
    projetos = projeto_model.Projeto.query.all()
    return projetos

# metodo para editar uma projeto a partir do seu ID
def editar_projeto(projeto_bd, projeto_novo):
    projeto_bd.nome = projeto_novo.nome
    projeto_bd.descricao = projeto_novo.descricao
    projeto_bd.funcionarios = []
    for i in projeto_novo.funcionarios:
        funcionario = listar_funcionario_id(i)
        projeto_bd.funcionarios.append(funcionario)
    db.session.commit()

# metodo para excluir uma projeto a partir do seu ID
def excluir_projeto(projeto):
    db.session.delete(projeto)
    db.session.commit()




# metodo para listar uma projeto pelo seu ID
def listar_projeto_id(id):
    projeto = projeto_model.Projeto.query.filter_by(id=id).first() #aplicando a query com filtro
    return projeto