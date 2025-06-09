from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from .controllers import get_usuario_by_id, novo_usuario, autenticar_usuario, atualizar_usuario, excluir_usuario, get_usuarios

bp_usuario = Blueprint('usuario', __name__)

@bp_usuario.route('/')
def index():
    return render_template('index.html')


@bp_usuario.route('/login')
def login():
    proxima = request.args.get('proxima')
    
    return render_template('login.html', proxima=proxima)

@bp_usuario.route('/autenticar', methods=['POST'])
def autenticar():
    nickname = request.form['nickname']
    senha = request.form['senha']
    
    if not nickname or not senha:
        flash('Usuário e senha são obrigatórios.')
        return redirect(url_for('usuario.login'))
    
    try:
        usuario_autenticado = autenticar_usuario(nickname, senha)
        
        session['usuario'] = usuario_autenticado.nickname  # Armazena o nickname do usuário na sessão
        flash(f'Bem vindo, {usuario_autenticado.nome}!')
    except ValueError as e:
        flash(str(e))    
    
    return redirect(url_for('jogo.index')) # Redireciona para a página anterior após o login

@bp_usuario.route('/logout')
def logout():
    session.pop('usuario', None) # Remove o usuário da sessão
    flash('Logout realizado com sucesso!')
    return redirect(url_for('index'))

@bp_usuario.route('/cadastro')
def registrar():
    return render_template('cadastro.html') 
