from abc import ABC, abstractmethod


class PaginaBase(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    @abstractmethod
    def renderizar(self):
        pass
