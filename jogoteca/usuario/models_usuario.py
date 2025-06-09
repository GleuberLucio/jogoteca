
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
    
    @classmethod
    def get_usuario_by_nickname(cls, nickname):
        """ Método para obter um usuário pelo nickname."""
        return cls.query.filter_by(nickname=nickname).first()
    
    @classmethod
    def criar_usuario(cls, nome, nickname, senha):
        """ Método para criar um novo usuário."""
        if cls.get_usuario_by_nickname(nickname):
            raise ValueError("Nickname já está em uso.")
        
        novo_usuario = cls(nome=nome, nickname=nickname, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario
    
    @classmethod
    def autenticar_usuario(cls, nickname, senha):
        """ Método para autenticar um usuário."""
        usuario = cls.get_usuario_by_nickname(nickname)
        if usuario and usuario.senha == senha:
            return usuario
        else:
            raise ValueError("Nickname ou senha incorretos.")
        
    @classmethod
    def atualizar_usuario(cls, id, nome=None, nickname=None, senha=None):
        """ Método para atualizar os dados de um usuário."""
        usuario = cls.query.get(id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        if nome:
            usuario.nome = nome
        if nickname:
            if cls.get_usuario_by_nickname(nickname) and cls.get_usuario_by_nickname(nickname).id != id:
                raise ValueError("Nickname já está em uso.")
            usuario.nickname = nickname
        if senha:
            usuario.senha = senha
        
        db.session.commit()
        return usuario
    
    @classmethod
    def excluir_usuario(cls, id):
        """ Método para excluir um usuário."""
        usuario = cls.query.get(id)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        db.session.delete(usuario)
        db.session.commit()
        return usuario