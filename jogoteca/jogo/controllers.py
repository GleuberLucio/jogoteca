from .models_jogo import Jogo
from config import Config
import os

def get_jogos():
    """Função para obter todos os jogos com suas capas."""
    jogos = Jogo.get_jogos()
    
    # Criar uma lista de jogos com informações da capa
    jogos_json = []
    for jogo in jogos:
        capa_jogo = buscar_capa_jogo(jogo.id)
        jogo_dict = {
            'id': jogo.id,
            'nome': jogo.nome,
            'ano': jogo.ano,
            'desenvolvedora': jogo.desenvolvedora,
            'genero': jogo.genero,
            'plataforma': jogo.plataforma,
            'capa': capa_jogo
        }
        jogos_json.append(jogo_dict)
    
    return jogos_json

def criar_novo_jogo(nome, ano, desenvolvedora, genero, plataforma):
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

def salvar_capa_jogo(arquivo, novo_jogo):
    # Verificar se um arquivo foi enviado
    if not arquivo or arquivo.filename == '':
        print("Nenhum arquivo foi enviado")
        return None
    
    upload_path = Config.UPLOADS_PATH
    
    # Verificar se a pasta de upload existe
    if not os.path.exists(upload_path):
        try:
            os.makedirs(upload_path)
            print(f'Pasta de upload criada: {upload_path}')
        except Exception as e:
            error_msg = f"Erro ao criar pasta de upload: {str(e)}"
            print(error_msg)
            raise ValueError(error_msg)
    
    # Obter a extensão do arquivo original
    nome_arquivo = arquivo.filename
    extensao = os.path.splitext(nome_arquivo)[1].lower()
    print(f'Arquivo enviado: {nome_arquivo}')
    print(f'Extensão detectada: {extensao}') 
    
    # Verificar se a extensão é válida
    extensoes_permitidas = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']
    if extensao not in extensoes_permitidas:
        error_msg = f"Formato não suportado: {extensao}. Formatos aceitos: {', '.join(extensoes_permitidas)}"
        print(error_msg)
        raise ValueError(error_msg)
    
    # Salvar o arquivo com a extensão correta
    nome_arquivo_salvo = f'capa{novo_jogo.id}{extensao}'
    caminho_completo = f'{upload_path}/{nome_arquivo_salvo}'
    
    try:
        arquivo.save(caminho_completo)
        print(f'Arquivo salvo com sucesso: {caminho_completo}')
        return nome_arquivo_salvo
    except Exception as e:
        error_msg = f"Erro ao salvar arquivo: {str(e)}"
        print(error_msg)
        raise ValueError(error_msg)
    
def buscar_capa_jogo(id):
    upload_path = Config.UPLOADS_PATH
    extensoes_permitidas = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']
    
    # Buscar arquivo com qualquer extensão válida
    for nome_arquivo in os.listdir(upload_path):
        for extensao in extensoes_permitidas:
            if f'capa{id}{extensao}' == nome_arquivo:
                return nome_arquivo
    
    return 'capa_padrao.jpg'

def filtrar_por_plataforma(plataforma):
    
    try: 
        jogos = Jogo.query.filter(Jogo.plataforma.ilike(f'%{plataforma}%')).all()
        jogos_filtrados = []
        for jogo in jogos:
            capa_jogo = buscar_capa_jogo(jogo.id)
            jogo_dict = {
                'id' : jogo.id,
                'nome' : jogo.nome,
                'ano' : jogo.ano,
                'genero' : jogo.genero,
                'plataforma' : jogo.plataforma,
                'capa' : capa_jogo
            }
            jogos_filtrados.append(jogo_dict)
        
        return jogos_filtrados
    except Exception as e:
        print(f'Erro ao filtrar jogos por plataforma: {str(e)}')
        return []