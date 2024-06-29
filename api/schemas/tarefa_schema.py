from api import ma
from ..models import tarefa_model
from marshmallow import fields
'''
    os schemas é quem vai traduzir os dados em json
    em uma linguagem que o paython entenda, para isso
    vamos usar a biblioteca marschmallow, para fazer essa
    conversão dos tipos de linguagem
    SQLAlchemyAutoSchema - usado para versoes acima da 1.1.1 
'''

class TarefaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        model = tarefa_model.Tarefa
        # informações que serão renderizadas
        fields = ('id', 'titulo', 'descricao', 'data_expiracao', 'projeto', '_links') # adicionar _links que esta com problema de serialização

    # colocando as restricoes dos dados
    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True)
    projeto = fields.String(required=True)
    
    #NOTE - Implementação de HATEOS
    _links = ma.Hyperlinks(
        {
            'get': ma.URLFor("tarefadetail", values=dict(id='<id>')),
            'put': ma.URLFor("tarefadetail", values=dict(id='<id>')),
            'delete': ma.URLFor("tarefadetail", values=dict(id='<id>'))
        }
    )