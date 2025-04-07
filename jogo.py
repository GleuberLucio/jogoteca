
class Jogo:
    def __init__(self, nome:str, ano:int, desenvolvedora:str, genero:str, plataforma:str, capa:str=None):
        """
        Inicializa um objeto Jogo com os atributos fornecidos.
        :param nome: Nome do jogo
        :param ano: Ano de lançamento do jogo
        :param desenvolvedora: Nome da desenvolvedora do jogo
        :param genero: Gênero do jogo
        :param plataforma: Plataforma do jogo
        :param capa: Caminho para a imagem da capa do jogo
        """
        
        self.nome = nome
        self.ano = ano
        self.desenvolvedora = desenvolvedora
        self.genero = genero
        self.plataforma = plataforma
        self.capa = capa

    def __str__(self):
        return f"Nome: {self.nome}, Ano: {self.ano}, Desenvolvedora: {self.desenvolvedora}, Genero: {self.genero}, Plataforma: {self.plataforma}"