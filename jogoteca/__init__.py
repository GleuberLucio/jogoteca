from flask import Flask
from db_init import db
from config import Config
from jogoteca.jogo.routes import bp_jogo
from jogoteca.usuario.routes import bp_usuario

app = Flask(__name__)

def create_app():
    app.config.from_object(Config)
        
    db.init_app(app)
    
    # Registros das blueprints
    app.register_blueprint(bp_jogo, url_prefix='/jogos')
    app.register_blueprint(bp_usuario)

    return app
