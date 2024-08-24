class Circo:

    def apresentar(self, tipo) -> None:
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self) -> None:
        print("Apresentando o malabarista.")

    def apresentar_palhaco(self) -> None:
        print("Apresentando o palhaço.")

circo = Circo()
circo.apresentar(2)