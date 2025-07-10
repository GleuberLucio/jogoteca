import os

class Config:
    """Configurações gerais da aplicação."""
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 's3nh4d3s3gur4'

    SQLALCHEMY_DATABASE_URI = \
            '{SGBD}://{usuario}:{senha}@{host}/{banco}'.format(
                SGBD='mysql+pymysql',
                usuario='root',
                senha='admin',
                host='localhost',
                banco='jogoteca'
            )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_NAME = 'session_cookie'
    UPLOADS_PATH = os.path.dirname(os.path.abspath(__file__)) + '/jogoteca/uploads'