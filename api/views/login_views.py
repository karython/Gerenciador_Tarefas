from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from api.schemas.login_schema import LoginSchema
from ..services import usuario_service
from flask_jwt_extended import create_access_token
from datetime import timedelta

class LoginList(Resource):
    def post(self):
        # instanciando o schema de login para nao perder a requisição do nome do usuario
        ls = LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            senha = request.json['senha']
            usuario_bd = usuario_service.lista_usuario(email)
            #verifica se o usuario existe e se a senha esta igual a senha criptrografada
            if usuario_bd and usuario_bd.verificar_senha(senha):
                # esse metodo ira gerar um token para o usuario ao fazer o login
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    #tempo de expiração do token
                    expires_delta=timedelta(minutes=5)
                )
                # se a verificação for bem sucedida ira retornar um access token valido por 60 segundos
                return make_response(jsonify({
                    'access_token': access_token,
                    'message': 'login realizado com sucesso'
                }), 200)
            # se não mostra mensagem de erro
            return make_response(jsonify({
                'message': 'Credenciais inválidas'
            }), 401)

api.add_resource(LoginList, '/login')