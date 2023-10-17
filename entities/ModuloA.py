from .Operacion import Operacion
from .CustomException import CustomException
from random import randint


class ModuloA(Operacion):
    """
    La funcionalidad es obtener un numero en el rango de 1 a 3.
    Se simula un fallo cuando el valor es 2.
    """

    def __init__(self) -> None:
        pass

    def ejecutar(self) -> int:
        random_number = randint(1, 3)
        print(f"[A] - El valor es {random_number}")
        if random_number == 2:
            raise CustomException("El valor aleatorio es 2")
        return random_number
