from abc import ABCMeta
from abc import abstractmethod


class Operacion(metaclass=ABCMeta):
    @abstractmethod
    def ejecutar(self):
        pass
