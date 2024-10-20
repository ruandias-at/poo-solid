from abc import ABC, abstractmethod

class AveVoadora(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'
    
class AveTerrestre(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'