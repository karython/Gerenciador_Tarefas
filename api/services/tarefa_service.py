from ..models import tarefa_model
from api import db

'''
    esse modulo de serviço fica responsavel por adicionar uma nova tarefa no banco de dados
    usando o sqlalchemy, usando o add e o commit para fazer o salvamento de dados e retorna a tarefa
'''

# metodo para cadastrar uma nova tarefa
def cadastrar_tarefa(tarefa):
    tarefa_bd = tarefa_model.Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao,
                                    data_expiracao=tarefa.data_expiracao, projeto=tarefa.projeto)

    db.session.add(tarefa_bd)
    db.session.commit()
    return tarefa_bd


# metodo para listar todas as tarefas
def listar_tarefas():
    tarefas = tarefa_model.Tarefa.query.all()
    return tarefas

# metodo para editar uma tarefa a partir do seu ID
def editar_tarefa(tarefa_bd, tarefa_nova):
    tarefa_bd.titulo = tarefa_nova.titulo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    tarefa_bd.projeto = tarefa_nova.projeto
    db.session.commit()



# metodo para excluir uma tarefa a partir do seu ID
def excluir_tarefa(tarefa):
    db.session.delete(tarefa)
    db.session.commit()




# metodo para listar uma tarefa pelo seu ID
def listar_tarefa_id(id):
    tarefa = tarefa_model.Tarefa.query.filter_by(id=id).first() #aplicando a query com filtro
    return tarefa