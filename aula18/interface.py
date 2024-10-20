from abc import ABC, abstractmethod

class Ave(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'