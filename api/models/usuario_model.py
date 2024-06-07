from api import db
from passlib.hash import pbkdf2_sha256

'''
    Este modulo é o que vai criar a tabela, esta com a estrutura da tabela
'''
class Usuario(db.Model):
    __tablename__ = "usuario"

    # Criando campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)



    #FIXME: esse metodo é para cripitocrafar a senha antes de salvar no banco
    def gen_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)


    # criptografa a senha informada e verifica se é igual a que foi salva no banco de dados
    def verificar_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)
