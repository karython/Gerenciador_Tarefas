from api import db
from ..models.projeto_model import Projeto

'''
    Este modulo é o que vai criar a tabela, esta com a estrutura da tabela
'''
class Tarefa(db.Model):
    __tablename__ = "tarefa"

    # Criando campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_expiracao = db.Column(db.Date, nullable=False)

    # Relacionamento com a tabela projeto
    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'), nullable=False)
    projeto = db.relationship(Projeto, backref=db.backref("tarefas", lazy="dynamic"))
