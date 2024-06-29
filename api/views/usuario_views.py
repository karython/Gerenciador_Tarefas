from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service


class UsuarioList(Resource):
    def post(self):

        """
        Esta rota é responsavel por cadastrar um novo usuário
        ---
        parameters:
          - in: body
            name: Usuario
            description: Cadastrar novo usuário
            schema:
              type: object
              required:
                - nome
                - email
                - senha
              properties:
                nome:
                  type: string
                email:
                  type: string
                senha:
                  type: string

        responses:
            201: 
              description: Usuário cadastrado com sucesso
              schema:
                id: Usuario
                properties:
                  nome:
                    type: string
                  email:
                    type: string
                  senha:
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
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            email = request.json['email']
            senha = request.json['senha']
            usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha)
            result = usuario_service.cadastrar_usuario(usuario_novo)
            return make_response(jsonify(result), 201)

api.add_resource(UsuarioList, '/usuario')