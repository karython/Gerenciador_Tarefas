from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

#FIXME: esse modulo esta sendo usado para fazer as configurações de importação para a API

app = Flask(__name__)

#usando o aquivo de configuração, onde esta todas as configurações do projeto

app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
JWTManager(app)

api = Api(app)


from .views import tarefa_views, projeto_views, funcionario_views, usuario_views, login_views
from .models import tarefa_model, projeto_model, funcionario_model, usuario_model