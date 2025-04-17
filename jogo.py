from sqlalchemy import Column, Integer, String
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