from flask_restful import Resource
from api import api
from ..schemas import projeto_schema
from flask import request, make_response, jsonify
from ..entidades import projeto
from ..services import projeto_service
from ..pagination import pagination
from ..models.projeto_model import Projeto

class ProjetoList(Resource):

    # funcao que ira chamar os metodos GET dos service
    # Listar todos os projetos
    def get (self):

        """
        Listagem de todos os projetos
        ---
        parameters:
          - in: header
            name: Authorization
            type: string
            required: true

        responses:
            200:
              description: Lista de todos os projetos
              schema:
                id: Projeto
                properties:
                  projeto_id:
                    type: integer
                  nome:
                    type: string
                  descricao:
                    type: string
                  tarefas:
                    type: string


        """
        
        #projetos = projeto_service.listar_projeto()
        ps = projeto_schema.ProjetoSchema(many=True)
        
        return pagination(Projeto, ps)


    # funcao que irar chamar os metodos POST (SET) dos service
    # criar novo projeto
    def post(self):

        """
        Esta rota é responsavel por cadastrar um novo projeto
        ---
        parameters:
          - in: body
            name: Projeto
            description: Criar novo projeto
            schema:
              type: object
              required:
                - nome
                - descricao
              properties:
                nome:
                  type: string
                descricao:
                  type: string

        responses:
            201: 
              description: Projeto criado com sucesso
              schema:
                id: Projeto
                properties:
                  nome:
                    type: string
                  descricao:
                    type: string

            400: 
              description: Erro na requisição
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Erro na requisição. Verifique os dados enviados                
            


        """
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json)

        # fazendo a validacao dos dados
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            funcionarios = request.json['funcionarios']
            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao, funcionarios=funcionarios)
            result = projeto_service.cadastrar_projeto(projeto_novo)
            return make_response(ps.jsonify(result), 201)


class ProjetoDetail(Resource):

    # Listar projetos por ID
    def get(self, id):

        """
        Retorna o projeto que possui o ID como parâmetro
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
              description: Projeto que possui o ID enviado
              schema:
                id: Projeto
                properties:
                  projeto_id:
                    type: integer
                  nome:
                    type: string
                  descricao:
                    type: string

            404: 
              description: Projeto não encontrado


        """
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("projeto não encontrada"), 404)
        ps = projeto_schema.ProjetoSchema()
        #uso do make_response me permite passar um condigo para verificar o status da solicitação
        return make_response(ps.jsonify(projeto), 200)

    # Editar projeto
    def put(self, id):

        """
        Retorna o projeto que possui o ID passado como parâmetro
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
          - in: body
            name: Projeto
            description: Editar projeto
            schema:
              type: object
              required:
                - nome
                - descricao
              properties:
                nome:
                  type: string
                descricao:
                  type: string

        responses:
            200: 
              description: Projeto editado com sucesso
              schema:
                id: Projeto
                properties:
                  nome:
                    type: string
                  descricao:
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
              description: Projeto não encontrada
        

         
        """
        projeto_bd = projeto_service.listar_projeto_id(id)

        # verificando se a projeto existe no banco
        if projeto is None:
            return make_response(jsonify("projeto não encontrada"), 404)
        ps = projeto_schema.ProjetoSchema()

        #passando a verificacao dos dados
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']

            projeto_novo = projeto.Projeto(nome=nome,
                                        descricao=descricao
                                        )

            # chamando a função para editar algum item
            projeto_service.editar_projeto(projeto_bd, projeto_novo)
            projeto_atualizado = projeto_service.listar_projeto_id(id)
            return make_response(ps.jsonify(projeto_atualizado), 200)

    # Deletando projeto
    def delete(self, id):

        """
        Remove o projeto que possui o ID como parâmetro
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true

        responses:
            204:
              description: Projeto removido com sucesso
            404: 
              description: Projeto não encontrado
        """
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("projeto não encontrada"), 404)
        projeto_service.excluir_projeto(projeto)
        return make_response(' ', 204)




# retornando os recursos, que sao os metodos que estao dentro da class, acessados atraves da rota projeto
api.add_resource(ProjetoList, '/projeto', endpoint='projeto_list')
api.add_resource(ProjetoDetail, '/projeto/<int:id>', endpoint='projeto_detail')
