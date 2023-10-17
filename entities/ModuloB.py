from .Operacion import Operacion
from random import randint


class ModuloB(Operacion):
    """
    La funcionalidad es obtener un numero en el rango de 1 a 3.
    Este modulo no falla.
    """

    def __init__(self) -> None:
        pass

    def ejecutar(self) -> int:
        random_number = randint(1, 3)
        print(f"[B] - El valor es {random_number}")
        return random_number
