class Pessoa:

    def __init__ (self, name: str, idade: int) -> None:
        self.name = name
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print(f"{self.name} está dirigindo um(a) {veiculo}.")

    def cantar(self) -> None:
        print("Lalarala")

    def apresentar_idade(self) -> str:
        return self.idade


