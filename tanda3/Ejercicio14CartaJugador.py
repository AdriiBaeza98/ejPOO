"""
Propósito: crea la clase CardPlayer que simule un jugador de naipes. Un jugador tiene un conjunto de naipes.

- Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
- Puede deshacerse de una carta.
- Puede recibir cartas.

Autor: Adrián Baeza

Fecha: 28/02/2023
"""

from typing import List
from typeguard import typechecked
from Ejercicio14Carta import Carta
from Ejercicio14Baraja import Baraja


@typechecked
class CartaJugador:

    def __init__(self, nombre: str):
        self.__nombrejugador = nombre
        self.__cartas = []

    @property
    def nombrejugador(self):
        return self.__nombrejugador

    @property
    def cartas(self):
        return self.__cartas.copy()

    def recibir(self, cartas: List[Carta]):
        self.__cartas.extend(cartas)

    def robar(self, baraja: Baraja):
        carta = baraja.robar()
        self.__cartas.append(carta)

    def tirar_carta(self, carta: Carta):
        if carta not in self.__cartas:
            raise ValueError(f"El jugador no puede deshacerse de una carta que no tiene")
        self.__cartas.remove(carta)

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre: {self.__nombrejugador}, cartas: {self.__cartas})"
