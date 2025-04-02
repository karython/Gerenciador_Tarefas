from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service


class UsuarioList(Resource):
    
    def get(self):
        """
        Esta rota é responsavel por listar todos os usuários
        ---
        responses:
            200: 
              description: Usuários encontrados com sucesso
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
        result = usuario_service.listar_usuarios()
        # make_response(): Cria uma resposta HTTP personalizada.
        return make_response(jsonify(result), 200)
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

        
        '''
        cria uma instancia do UsuarioSchema, que é um schema do Marshmallow.
        O schema (UsuarioSchema) é responsável por 
        validar os dados enviados na requisição (request.json) e garantir que estejam no formato correto.

        usa o metodo validate verifica se os campos obrigatórios 
        estão presentes e se os valores estão no formato correto.

        trata o erro de validação, retornando uma resposta JSON com o erro e o status 400 (Bad Request).
        Se a validação passar, ele cria um novo objeto Usuario com os dados fornecidos na requisição.
        '''
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

'''
é uma parte essencial do Flask-RESTful. Ele registra a classe UsuarioList 
como um recurso da API e define a URL onde esse recurso estará disponível.
'''
api.add_resource(UsuarioList, '/usuario')