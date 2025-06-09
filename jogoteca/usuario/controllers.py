from .models_usuario import Usuario

def get_usuarios():
    """Função para obter todos os usuários."""
    return Usuario.query.all()

def get_usuario_by_id(usuario_id):
    """Função para obter um usuário pelo ID."""
    usuario = Usuario.query.get(usuario_id)
    if usuario:
        return usuario
    else:
        raise ValueError(f"Usuário com ID {usuario_id} não encontrado.")
    
def novo_usuario(nome, nickname, senha):
    """Função para criar um novo usuário."""
    return Usuario.criar_usuario(nome, nickname, senha)

def autenticar_usuario(nickname, senha):
    """Função para autenticar um usuário."""
    return Usuario.autenticar_usuario(nickname, senha)

def atualizar_usuario(usuario_id, nome=None, nickname=None, senha=None):
    """Função para atualizar os dados de um usuário."""
    return Usuario.atualizar_usuario(usuario_id, nome, nickname, senha)

def excluir_usuario(usuario_id):
    """Função para excluir um usuário pelo ID."""
    return Usuario.excluir_usuario(usuario_id)

def get_usuario_by_nickname(nickname):
    """Função para obter um usuário pelo nickname."""
    return Usuario.get_usuario_by_nickname(nickname)

