from api import ma
from api.models import funcionario_model
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
'''
    os schemas é quem vai traduzir os dados em json
    em uma linguagem que o paython entenda, para isso
    vamos usar a biblioteca marschmallow, para fazer essa
    conversão dos tipos de linguagem
    SQLAlchemyAutoSchema - usado para versoes acima da 1.1.1 
'''

#TODO: problema de serializacao json, precisa ainda adicionar a lista de projetos

class FuncionarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = funcionario_model.Funcionario
        # informações que serão renderizadas
        fields = ('id', 'nome', 'dtNascimento', 'cpf')#adicionar projeto


    # colocando as restricoes dos dados
    nome = fields.String(required=True)
    dtNascimento = fields.Date(required=True)
    cpf = fields.String(required=True)
