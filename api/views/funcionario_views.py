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
        #funcionarios = funcionario_service.listar_funcionarios()
        fs = funcionario_schema.FuncionarioSchema(many=True)
        return pagination(Funcionario, fs)


    # funcao que irar chamar os metodos POST (SET) dos service
    def post(self):
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
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("funcionario não encontrada"), 404)
        fs = funcionario_schema.FuncionarioSchema()
        #uso do make_response me permite passar um condigo para verificar o status da solicitação
        return make_response(fs.jsonify(funcionario), 200)


    def put(self, id):
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
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("funcionario não encontrada"), 404)
        funcionario_service.excluir_funcionario(funcionario)
        return make_response('', 204)




# retornando os recursos, que sao os metodos que estao dentro da class, acessados atraves da rota funcionarios
api.add_resource(FuncionarioList, '/funcionario')
api.add_resource(FuncionarioDetail, '/funcionario/<int:id>')
