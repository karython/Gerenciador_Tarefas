from api import ma
from api.models import usuario_model
from marshmallow import fields

'''
    Foi nescessario a criação desse schema para criar validações diferentes
    de cadastro de usuario.
    Ex: ao cadastrar novo usaurio informa nome, email, e senha como required
    já para logar somente email e senha, para isso preciso criar o schema login
    para tirar o required somente de login
'''
class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = usuario_model.Usuario
        # informações que serão renderizadas
        fields = ('id', 'nome', 'email', 'senha')


    # colocando as restricoes dos dados
    nome = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)
