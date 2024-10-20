from abc import ABC, abstractmethod

class Repositorio(ABC):

    @abstractmethod
    def insert(self, dado: any) -> None:
        pass
    
    @abstractmethod
    def delete(self, dado: any) -> None:
        pass
