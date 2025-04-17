
from db_init import db


class Usuario(db.Model):
    """ Classe que representa um usuário na aplicação."""
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(20), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"<Usuario id={self.id}, nome={self.nome}, nickname={self.nickname}>"
    
    def __str__(self):
        return f"Nome: {self.nome}, Nickname: {self.nickname}"