class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)

    def __armazenar_usuario(self, nome: str, idade:int) -> None:
        print(f"Acessando o banco de dados...\nCadastrar o usuário {nome}, idade {idade}")

    def __indicar_erro(self) -> None:
        print("Dados Inválidos")

