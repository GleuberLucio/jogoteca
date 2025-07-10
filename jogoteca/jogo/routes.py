from flask import Blueprint, render_template, request, redirect, session, flash, url_for, send_from_directory, jsonify
from .controllers import *

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
    
    return render_template('novo.html', titulo='Novo Jogo')

@bp_jogo.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    ano = request.form['ano']
    desenvolvedora = request.form['desenvolvedora']
    genero = request.form['genero']
    plataforma = request.form['plataforma']

    novo_jogo = criar_novo_jogo(nome, ano, desenvolvedora, genero, plataforma)
    arquivo = request.files['arquivo']
    salvar_capa_jogo(arquivo, novo_jogo)
    
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
        arquivo = request.files['arquivo']

        try:
            atualizar_jogo(id, nome, ano, desenvolvedora, genero, plataforma, capa)
            salvar_capa_jogo(arquivo, jogo)
            flash('Jogo atualizado com sucesso!')
            return redirect(url_for('jogo.index'))
        except ValueError as e:
            flash(str(e))
            return redirect(url_for('jogo.editar', id=id))
    
    if not jogo:
        flash('Jogo não encontrado.')
        return redirect(url_for('jogo.index'))
    
    capa_jogo = buscar_capa_jogo(jogo.id)
    
    return render_template('editar.html', titulo='Editar Jogo', jogo=jogo, capa_jogo=capa_jogo)

@bp_jogo.route('/excluir/id=<int:id>', methods=['POST'])
def excluir(id):
    try:
        excluir_jogo(id)
        flash('Jogo deletado com sucesso!')
    except ValueError as e:
        flash(str(e))
    
    return redirect(url_for('jogo.index'))

@bp_jogo.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)

@bp_jogo.route('/filtrar/<plataforma>')
def filtro_plataforma(plataforma):
    print(f'Plataforma: {plataforma}')
    jogos_filtrados = filtrar_por_plataforma(plataforma)
    return jsonify({
        'success': True,
        'jogos': jogos_filtrados,
        'total': len(jogos_filtrados)
    })

@bp_jogo.route('/api/jogos')
def api_jogos():
    """Retorna todos os jogos em formato JSON"""
    jogos = get_jogos()
    return jsonify({
        'success': True,
        'jogos': jogos,
        'total': len(jogos)
    })