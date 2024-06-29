from flask_restful import Resource
from api import api
from ..schemas import funcionario_schema
from flask import request, make_response, jsonify
from ..entidades import funcionario
from ..services import funcionario_service
from ..pagination import pagination
from ..models.funcionario_model import Funcionario

class FuncionarioList(Resource):

    # funcao que ira chamar os metodos GET dos service
    def get (self):

        """
        Listagem de todos os funcionarios
        ---
        parameters:
          - in: header
            name: Authorization
            type: string
            required: true

        responses:
            200:
              description: Lista de todos os funcionarios
              schema:
                id: Funcionarios
                properties:
                  funcionario_id:
                    type: integer
                  nome:
                    type: string
                  dtNascimento:
                    type: string
                  cpf:
                    type: string


        """
        #funcionarios = funcionario_service.listar_funcionarios()
        fs = funcionario_schema.FuncionarioSchema(many=True)
        return pagination(Funcionario, fs)


    # funcao que irar chamar os metodos POST (SET) dos service
    def post(self):

        """
        Esta rota é responsavel por cadastrar um novo funcionario
        ---
        parameters:
          - in: body
            name: Funcionario
            description: Cadastrar novo funcionario
            schema:
              type: object
              required:
                - nome
                - dtNascimento
                - cpf
              properties:
                nome:
                  type: string
                dtNascimento:
                  type: string
                cpf:
                  type: string
                

        responses:
            201: 
              description: Funcionario cadastrado com sucesso
              schema:
                id: Funcionario
                properties:
                  nome:
                    type: string
                  dtNascimento:
                    type: string
                  cpf:
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
        fs = funcionario_schema.FuncionarioSchema()
        validate = fs.validate(request.json)

        # fazendo a validacao dos dados
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            dtNascimento = request.json['dtNascimento']
            cpf = request.json['cpf']
            funcionario_novo = funcionario.Funcionario(nome=nome, dtNascimento=dtNascimento, cpf=cpf)
            result = funcionario_service.cadastrar_funcionario(funcionario_novo)
            return make_response(fs.jsonify(result), 201)


class FuncionarioDetail(Resource):
    def get(self, id):

        """
        Retorna o funcionario que possui o ID como parâmetro
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
              description: Funcionario que possui o ID enviado
              schema:
                id: Funcionario
                properties:
                  funcionario_id:
                    type: integer
                  nome:
                    type: string
                  dtNascimento:
                    type: string
                  cpf:
                    type: string

            404: 
              description: funcionario não encontrado


        """
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("funcionario não encontrada"), 404)
        fs = funcionario_schema.FuncionarioSchema()
        #uso do make_response me permite passar um condigo para verificar o status da solicitação
        return make_response(fs.jsonify(funcionario), 200)


    def put(self, id):

        """
        Retorna o funcionario que possui o ID passado como parâmetro
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
          - in: body
            name: Funcionario
            description: Editar funcionario
            schema:
              type: object
              required:
                - nome
                - dtNascimento
                - cpf
              properties:
                nome:
                  type: string
                dtNascimento:
                  type: string
                cpf:
                  type: string

        responses:
            200: 
              description: Funcionario editado com sucesso
              schema:
                id: Funcionario
                properties:
                  nome:
                    type: string
                  dtNascimento:
                    type: string
                  cpf:
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
              description: Funcionario não encontrada
        

         
        """
        funcionario_bd = funcionario_service.listar_funcionario_id(id)

        # verificando se o funcionario existe no banco
        if funcionario is None:
            return make_response(jsonify("funcionario não encontrada"), 404)
        fs = funcionario_schema.FuncionarioSchema()

        #passando a verificacao dos dados
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            dtNascimento = request.json['dtNascimento']
            cpf = request.json['cpf']

            funcionario_novo = funcionario.Funcionario(nome=nome,
                                        dtNascimento=dtNascimento,
                                        cpf=cpf
                                        )

            # chamando a função para editar algum item
            funcionario_service.editar_funcionario(funcionario_bd, funcionario_novo)
            funcionario_atualizada = funcionario_service.listar_funcionario_id(id)
            return make_response(fs.jsonify(funcionario_atualizada), 200)


    def delete(self, id):

        """
        Remove o funcionario que possui o ID como parâmetro
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true

        responses:
            204:
              description: Funcionario removido com sucesso
            404: 
              description: Funcionario não encontrado
        """
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("funcionario não encontrada"), 404)
        funcionario_service.excluir_funcionario(funcionario)
        return make_response('', 204)




# retornando os recursos, que sao os metodos que estao dentro da class, acessados atraves da rota funcionarios
api.add_resource(FuncionarioList, '/funcionario')
api.add_resource(FuncionarioDetail, '/funcionario/<int:id>')
