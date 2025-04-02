from api.schemas.usuario_schema import UsuarioSchema
from ..models import usuario_model
from api import db

def cadastrar_usuario(usuario):
    usuario_db = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha()
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

def lista_usuario(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()

def listar_usuarios():
    usuarios = usuario_model.Usuario.query.all()
    schema = UsuarioSchema(many=True)  # Certifique-se de definir many=True
    return schema.dump(usuarios)