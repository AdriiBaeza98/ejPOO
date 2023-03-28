"""
Propósito: implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formas
de construir un dado (uno al que no se le pasa nada e inicializa el dado al azar, otro al que sólo
se le pasa que número tiene el dado en la cara superior y otro con el número del dado en la cara superior
y el número de caras del dado). Implementa los getters, el método roll() que tirará el dado al azar
y el __str__().

Autor: Adrián Baeza

Fecha: 08/02/2023
"""

import random
from typing import Optional
from typeguard import typechecked

CARAS_POR_DEFECTO = 6


@typechecked
class Dado:

    def __init__(self, cara: Optional[int] = None, num_caras: int = CARAS_POR_DEFECTO):

        if num_caras <= 0:
            raise ValueError(f"El dado no puede tener un número de caras negativo o 0. Recibido: {num_caras}")
        self.__num_caras = num_caras

        if cara is None:
            self.lanzar()
            return
        if cara <= 0 or cara > num_caras:
            raise ValueError(f"El valor de la cara no puede ser menor o igual a cero o mayor que"
                             f"su número de caras. Recibido: {cara}")
        self.__cara = cara

    @property
    def cara(self):
        return self.__cara

    @property
    def num_caras(self):
        return self.__num_caras

    def __str__(self):
        return str(self.__cara)

    def __repr__(self):
        return f"{self.__class__.__name__}(cara = {self.__cara}, num_caras = {self.__num_caras})"

    def lanzar(self):
        self.__cara = random.randint(1, CARAS_POR_DEFECTO)
        return self.__cara
