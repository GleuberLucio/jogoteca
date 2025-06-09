from db_init import db

class Jogo(db.Model):
    """ Classe que representa um jogo na aplicação."""
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.String(4), nullable=False)
    desenvolvedora = db.Column(db.String(40), nullable=False)
    genero = db.Column(db.String(20), nullable=False)
    plataforma = db.Column(db.String(20), nullable=False)
    capa = db.Column(db.String(300), nullable=True)
    
    def __repr__(self):
        return f"<Jogo id={self.id}, nome={self.nome}, ano={self.ano}>"
    
    def __str__(self):
        return f"Nome: {self.nome}, Ano: {self.ano}, Desenvolvedora: {self.desenvolvedora}, Genero: {self.genero}, Plataforma: {self.plataforma}"
    
    @classmethod
    def get_jogos(cls):
        """ Método para obter todos os jogos."""
        return cls.query.all()
    
    @classmethod
    def novo_jogo(cls, nome, ano, desenvolvedora, genero, plataforma):
        """ Método para criar um novo jogo."""
        novo_jogo = cls(nome=nome, ano=ano, desenvolvedora=desenvolvedora,
                        genero=genero, plataforma=plataforma)
        db.session.add(novo_jogo)
        db.session.commit()
        return novo_jogo
    
    @classmethod
    def save(cls, jogo):
        """ Método para salvar um jogo."""
        db.session.add(jogo)
        db.session.commit()
        return jogo
   
    @classmethod
    def delete(cls, jogo):
        """ Método para excluir um jogo."""
        db.session.delete(jogo)
        db.session.commit()
        return jogo