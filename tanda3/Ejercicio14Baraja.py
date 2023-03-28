"""
Propósito: crea la clase Deck que simula un conjunto de cartas de naipes.

- Inicialmente, tiene las cartas que le llegan con el constructor.
- Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
- Le pueden quitar la primera carta (robar).
- Puede barajarse.

Autor: Adrián Baeza

Fecha: 28/02/2023
"""

import random
from typing import List
from typeguard import typechecked
from Ejercicio14Carta import Carta


@typechecked
class Baraja:

    def __init__(self, cartas: List[Carta]):
        self.__cartas = list(cartas)

    @property
    def tamanno(self):
        return len(self.__cartas)

    def repartir(self, jugador, numero: int):
        if numero < 0:
            raise ValueError("No se puede repartir un número de cartas negativo")
        if numero > len(self.__cartas):
            raise ValueError("El número a repartir supera al número de cartas disponibles")

        cartas_a_repartir = self.__cartas[:numero]
        jugador.recibir(cartas_a_repartir)
        self.__cartas = self.__cartas[numero:]

    def robar(self):
        if self.tamanno == 0:
            raise ValueError("No quedan más cartas en la baraja")
        return self.__cartas.pop(0)

    def barajar(self):
        random.shuffle(self.__cartas)

    def __repr__(self):
        return repr(self.__cartas)
