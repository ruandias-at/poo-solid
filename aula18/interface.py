from abc import ABC, abstractmethod

class AveVoadora(ABC):

    @abstractmethod
    def comer(self) -> None:
        raise 'Should implement comer method'

    @abstractmethod
    def voar(self) -> None:
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self) -> None:
        raise 'Should implement gritar method'
    
class AveTerrestre(ABC):

    @abstractmethod
    def comer(self) -> None:
        raise 'Should implement comer method'

    @abstractmethod
    def gritar(self) -> None:
        raise 'Should implement gritar method'
