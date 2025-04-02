from api import ma
from api.models import usuario_model
from marshmallow import fields

'''
    os schemas é quem vai traduzir os dados em json
    em uma linguagem que o paython entenda, para isso
    vamos usar a biblioteca marschmallow, para fazer essa
    conversão dos tipos de linguagem
    SQLAlchemyAutoSchema - usado para versoes acima da 1.1.1 
'''


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = usuario_model.Usuario
        # informações que serão renderizadas

        
        '''
        Os fields no Marshmallow são utilizados para definir os tipos de dados que um schema deve aceitar e serializar.
        Se um usuário enviar um JSON errado, o UsuarioSchema bloqueia automaticamente.
        '''
        fields = ('id', 'nome', 'email', 'senha')


    # colocando as restricoes dos dados
    nome = fields.String(required=True)
    email = fields.String(required=True)
    senha = fields.String(required=True)
