from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from .controllers import get_jogos, novo_jogo, get_jogo_by_id, atualizar_jogo, excluir_jogo


bp_jogo = Blueprint('jogo', __name__)

@bp_jogo.route('/')
def index():
    jogos = get_jogos()
    if not jogos:
        flash('Nenhum jogo cadastrado.')
        return render_template('lista.html', titulo='Catálogo de Jogos', jogos=[])
    return render_template('lista.html', titulo='Catálogo de Jogos', jogos=jogos)

@bp_jogo.route('/novo')
def novo():
    # if 'usuario' not in session:
    #     flash('Você precisa fazer login para acessar esta página.')
    #     return redirect(url_for('login', proxima=url_for("jogo.novo")))
    
    return render_template('novo.html', titulo='Novo Jogo')

@bp_jogo.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    ano = request.form['ano']
    desenvolvedora = request.form['desenvolvedora']
    genero = request.form['genero']
    plataforma = request.form['plataforma']

    novo_jogo(nome, ano, desenvolvedora, genero, plataforma)
    
    return redirect(url_for('jogo.index'))

@bp_jogo.route('/editar/id=<int:id>', methods=['GET', 'POST'])
def editar(id):
    jogo = get_jogo_by_id(id)
    
    if request.method == 'POST':
        nome = request.form['nome']
        ano = request.form['ano']
        desenvolvedora = request.form['desenvolvedora']
        genero = request.form['genero']
        plataforma = request.form['plataforma']
        capa = request.form['url_capa'] 

        try:
            atualizar_jogo(id, nome, ano, desenvolvedora, genero, plataforma, capa)
            flash('Jogo atualizado com sucesso!')
            return redirect(url_for('jogo.index'))
        except ValueError as e:
            flash(str(e))
            return redirect(url_for('jogo.editar', id=id))
    
    if not jogo:
        flash('Jogo não encontrado.')
        return redirect(url_for('jogo.index'))
    
    return render_template('editar.html', titulo='Editar Jogo', jogo=jogo)

@bp_jogo.route('/excluir/id=<int:id>', methods=['POST'])
def excluir(id):
    try:
        excluir_jogo(id)
        flash('Jogo deletado com sucesso!')
    except ValueError as e:
        flash(str(e))
    
    return redirect(url_for('jogo.index'))