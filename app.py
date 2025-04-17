from flask import Flask, render_template, request, redirect, session, flash, url_for
from db_init import db
from jogo import Jogo
from usuario import Usuario


app = Flask(__name__)

app.secret_key = 's3nh4d3s3gur4'
app.config['SESSION_COOKIE_NAME'] = 'session_cookie'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{host}/{banco}'.format(
        SGBD='mysql+pymysql',
        usuario='root',
        senha='admin',
        host='localhost',
        banco='jogoteca'
    )
    
db.init_app(app)


@app.route('/')
def index():
    jogos = Jogo.query.order_by(Jogo.id)
    return render_template('lista.html', titulo='Jogos', jogos=jogos)

@app.route('/novo')
def novo():
    if 'usuario' not in session:
        flash('Você precisa fazer login para acessar esta página.')
        return redirect(url_for('login', proxima=url_for("novo")))
    
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    ano = request.form['ano']
    desenvolvedora = request.form['desenvolvedora']
    genero = request.form['genero']
    plataforma = request.form['plataforma']

    novo_jogo = Jogo(nome, ano, desenvolvedora, genero, plataforma)
    jogos.append(novo_jogo)
    # Salvar o novo jogo em um arquivo ou banco de dados.
    
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    proxima = request.form['proxima']
    if senha != '123':
        flash('Senha incorreta')
        return redirect(url_for('login'))


    # Aqui você deve implementar a lógica de autenticação.
    # Para fins de exemplo, vamos considerar que o login é sempre bem-sucedido.
    session['usuario'] = usuario
    flash(f'Bem vindo, {usuario}!')
    
    return redirect(proxima) # Redireciona para a página anterior após o login

@app.route('/logout')
def logout():
    session.pop('usuario', None) # Remove o usuário da sessão
    flash('Logout realizado com sucesso!')
    return redirect(url_for('index'))



app.run(host='0.0.0.0', port=8000, debug=True)