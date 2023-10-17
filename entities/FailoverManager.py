from .ModuloA import ModuloA
from .ModuloB import ModuloB
from .Operacion import Operacion


class FailoverManager:
    def __init__(self) -> None:
        # iniciar con primer ModuloA
        self.modulo_actual: Operacion = ModuloA()

    def do(self) -> int:
        return self.modulo_actual.ejecutar()

    def cambiar_modulo(self):
        # switch entre modulos
        if isinstance(self.modulo_actual, ModuloA):
            self.modulo_actual = ModuloB()
        else:
            self.modulo_actual = ModuloA()
