from api import db

'''
    Este modulo é o que vai criar a tabela, esta com a estrutura da tabela
'''
class Funcionario(db.Model):
    __tablename__ = "funcionario"

    # Criando campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    dtNascimento = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(50), nullable=False)

    # relacionando com a tabela funcionario_projeto
    projetos = db.relationship('Projeto', secondary='funcionario_projeto', back_populates='funcionarios')
