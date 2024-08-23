class MinhaClasse:

    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo!'
        self.meu_atributo2 = att

    def meu_metodo(self) -> None:
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num, mult) -> int:
        return num * mult


objeto = MinhaClasse(23)
objeto.meu_metodo()

