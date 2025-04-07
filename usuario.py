class Usuario:
    def __init__(self, nome, nickname, senha):
        """
        Inicializa um objeto Usuario com os atributos fornecidos.
        :param nome: Nome do usuário
        :param nickname: Apelido do usuário
        :param senha: Senha do usuário
        """
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
        
    def __str__(self):
        return f"Nome: {self.nome}, Nickname: {self.nickname}"