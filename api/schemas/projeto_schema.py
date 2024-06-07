from api import ma
from api.models import projeto_model
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
'''
    os schemas é quem vai traduzir os dados em json
    em uma linguagem que o paython entenda, para isso
    vamos usar a biblioteca marschmallow, para fazer essa
    conversão dos tipos de linguagem
    SQLAlchemyAutoSchema - usado para versoes acima da 1.1.1 
'''

#TODO: falta mostrar a lista de tarefas e funcionarios associadas a um determinado projeto


class ProjetoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = projeto_model.Projeto
        # informações que serão renderizadas
        fields = ('id', 'nome', 'descricao')#adicionar tarefas e funcionarios


    # colocando as restricoes dos dados
    nome = fields.String(required=True)
    descricao = fields.String(required=True)
