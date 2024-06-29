
#from flask_jwt_extended import jwt_required
from flask_restful import Resource
from api import api
from ..schemas import tarefa_schema
from flask import request, make_response, jsonify
from ..entidades import tarefa
from ..schemas.tarefa_schema import TarefaSchema
from ..services import tarefa_service, projeto_service
from ..pagination import pagination
from ..models.tarefa_model import Tarefa

class TarefaList(Resource):

    # esse comando que ira privar o metodo GET, so será possivel usando o token de acesso
    #FIXME atualizar a geração de token para privar os demais metodos
    #@jwt_required

    # funcao que ira chamar os metodos GET dos service
    def get (self):
        """
        Listagem de todas as tarefas
        ---
        parameters:
          - in: header
            name: Authorization
            type: string
            required: true

        responses:
            200:
              description: Lista de todas as tarefas
              schema:
                id: Tarefa
                properties:
                  tarefa_id:
                    type: integer
                  titulo:
                    type: string
                  descricao:
                    type: string
                  data_expiracao:
                    type: string
                  projeto:
                    type: string


        """

        # com a paginação, o metodo de listar tarefa não será usado (importar pagination e alterar return)
        # tarefas = tarefa_service.listar_tarefas()
        ts = tarefa_schema.TarefaSchema(many=True)
        return pagination(Tarefa, ts)


    # funcao que irar chamar os metodos POST (SET) dos service
    def post(self):
        """
        Esta rota é responsavel por cadastrar uma nova tarefa
        ---
        parameters:
          - in: body
            name: Tarefa
            description: Criar nova tarefa
            schema:
              type: object
              required:
                - titulo
                - descricao
                - data_expiracao
                - projeto
              properties:
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string

        responses:
            201: 
              description: Tarefa criada com sucesso
              schema:
                id: Tarefa
                properties:
                  titulo:
                    type: string
                  descricao:
                    type: string
                  data_expiracao:
                    type: string
                  projeto:
                    type: string

            400: 
              description: Erro na requisição
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Erro na requisição. Verifique os dados enviados                
            
            404: 
              description: Projeto não encontrado
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Projeto não encontrado


        """


        ts = TarefaSchema()
        validate = ts.validate(request.json)

        # fazendo a validacao dos dados
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            data_expiracao = request.json['data_expiracao']
            projeto = request.json['projeto']
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)

            if projeto_tarefa is None:
                return make_response(jsonify("Projeto não encontrada"), 404)

            tarefa_nova = tarefa.Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, projeto=projeto_tarefa)

            result = tarefa_service.cadastrar_tarefa(tarefa_nova)
            return make_response(ts.jsonify(result), 201)


class TarefaDetail(Resource):

    def get(self, id):
        """
        Retorna a tarefa que possui o ID como parâmetro
        ---
        parameters:
          - in: header
            name: Authorization
            type: string
            required: true
          - in: path
            name: id
            type: integer
            required: true

        responses:
            200:
              description: Tarefa que possui o ID enviado
              schema:
                id: Tarefa
                properties:
                  tarefa_id:
                    type: integer
                  titulo:
                    type: string
                  descricao:
                    type: string
                  data_expiracao:
                    type: string
                  projeto:
                    type: string

            404: 
              description: Tarefa não encontrada


        """
        tarefa = tarefa_service.listar_tarefa_id(id)
        if tarefa is None:
            return make_response(jsonify("tarefa não encontrada"), 404)
        ts = tarefa_schema.TarefaSchema()
        #uso do make_response me permite passar um condigo para verificar o status da solicitação
        return make_response(ts.jsonify(tarefa), 200)


    def put(self, id):

        """
        Retorna a tarefa que possui o ID passado como parâmetro
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
          - in: body
            name: Tarefa
            description: Editar tarefa
            schema:
              type: object
              required:
                - titulo
                - descricao
                - data_expiracao
                - projeto
              properties:
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string

        responses:
            200: 
              description: Tarefa editada com sucesso
              schema:
                id: Tarefa
                properties:
                  titulo:
                    type: string
                  descricao:
                    type: string
                  data_expiracao:
                    type: string
                  projeto:
                    type: string

            400: 
              description: Erro na requisição
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Erro na requisição. Verifique os dados enviados
            
            404: 
              description: Tarefa não encontrada
        

         
        """

        tarefa_bd = tarefa_service.listar_tarefa_id(id)

        # verificando se a tarefa existe no banco
        if tarefa is None:
            return make_response(jsonify("tarefa não encontrada"), 404)
        ts = tarefa_schema.TarefaSchema()

        #passando a verificacao dos dados
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            data_expiracao = request.json['data_expiracao']
            projeto = request.json['projeto']
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)

            if projeto_tarefa is None:
                return make_response(jsonify("Projeto não encontrada"), 404)

            tarefa_nova = tarefa.Tarefa(titulo=titulo,
                                        descricao=descricao,
                                        data_expiracao=data_expiracao,
                                        projeto=projeto_tarefa)

            # chamando a função para editar algum item
            tarefa_service.editar_tarefa(tarefa_bd, tarefa_nova)
            tarefa_atualizada = tarefa_service.listar_tarefa_id(id)
            return make_response(ts.jsonify(tarefa_atualizada), 200)


    def delete(self, id):
        """
        Remove a tarefa que possui o ID como parâmetro
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true

        responses:
            204:
              description: Tarefa removida com sucesso
            404: 
              description: Tarefa não encontrada
        """

        tarefa = tarefa_service.listar_tarefa_id(id)
        if tarefa is None:
            return make_response(jsonify("tarefa não encontrada"), 404)
        tarefa_service.excluir_tarefa(tarefa)
        return make_response(' ', 204)




# retornando os recursos, que sao os metodos que estao dentro da class, acessados atraves da rota tarefas
api.add_resource(TarefaList, '/tarefa')
api.add_resource(TarefaDetail, '/tarefa/<int:id>', endpoint='tarefadetail')
