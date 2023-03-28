"""
Propósito: implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor,
tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades.
Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre
el área y perímetro de dicho rectángulo.

Autor: Adrián Baeza

Fecha: 07/02/2023
"""

from Ejercicio2 import Punto
from typeguard import typechecked


@typechecked
class Rectangulo:

    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, value: Punto):
        self.__p1 = value

    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, value: Punto):
        self.__p2 = value

    @property
    def area(self):
        return abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))

    @property
    def perimetro(self):
        return 2 * abs(self.p1.x - self.p2.x) + 2 * abs(self.p1.y - self.p2.y)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.p1}, {self.p2})"
