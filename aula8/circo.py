class Circo:

    def apresentar(self, apresentador: any) -> None:
        apresentador.apresentar_show()


class Malabarista:
    def apresentar_show(self) -> None:
        print("Malabarista apresentando seu show.")


class Palhaco:
    def apresentar_show(self) -> None:
        print("Palhaco apresentando seu show.")


class Domador:
    def apresentar_show(self) -> None:
        print("Domador apresentando seu show.")

circo = Circo()
malabar = Malabarista()
coringa = Palhaco()
circo.apresentar(coringa)