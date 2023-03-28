"""
Propósito: crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6
que tienen la misma probabilidad de salir y un programa de prueba.

Autor: Adrián Baeza

Fecha: 26/01/2023
"""

import random


class Dado:
    def __init__(self):
        self.__cara = 0

    @property  # Getter como propiedad, para poder mostrar la cara del dado
    def cara(self):
        return self.__cara

    def __str__(self):
        return str(self.__cara)

    def lanzar(self):
        self.__cara = random.randint(1, 6)
