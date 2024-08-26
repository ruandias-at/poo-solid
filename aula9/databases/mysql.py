class MySQLDB:

    def __init__(self) -> None:
        self.__conexao = 'MySQL'

    def conectar(self) -> str:
        print("Conectando ao banco MySQL...")
        return self.__conexao
    
    def desconectar(self) -> str:
        print("Desconectando do banco MySQL...")
        return self.__conexao
