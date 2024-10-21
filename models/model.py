class Login:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.__senha__ = senha

    def getSenha(self):
        return self.__senha__


logado= Login("matheus","1234")
