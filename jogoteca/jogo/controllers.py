from .models_jogo import Jogo

def get_jogos():
    """Função para obter todos os jogos."""
    return Jogo.get_jogos()

def novo_jogo(nome, ano, desenvolvedora, genero, plataforma):
    """Função para criar um novo jogo."""
    return Jogo.novo_jogo(nome, ano, desenvolvedora, genero, plataforma)

def get_jogo_by_id(jogo_id):
    """Função para obter um jogo pelo ID."""
    jogo = Jogo.query.get(jogo_id)
    if jogo:
        return jogo
    else:
        raise ValueError(f"Jogo com ID {jogo_id} não encontrado.")
    
def atualizar_jogo(jogo_id, nome, ano, desenvolvedora, genero, plataforma, capa=None):
    """Função para atualizar um jogo existente."""
    jogo = get_jogo_by_id(jogo_id)
    jogo.nome = nome
    jogo.ano = ano
    jogo.desenvolvedora = desenvolvedora
    jogo.genero = genero
    jogo.plataforma = plataforma
    jogo.capa = capa
    Jogo.save(jogo)
    return jogo

def excluir_jogo(jogo_id):
    """Função para excluir um jogo pelo ID."""
    jogo = get_jogo_by_id(jogo_id)
    Jogo.delete(jogo)
    return jogo

