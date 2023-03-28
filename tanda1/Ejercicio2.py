"""
Propósito: implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor,
los getters y setters (propiedades), un invert_coordinates() que invierta las coordenadas x e y del punto.
Además, la clase debe tener un __str__() para poder imprimir los puntos en formato “(x, y)”.
Implementa un test donde crees un punto, lo imprimas utilizando de manera implícita el método __str__(),
imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a imprimir el punto.

Autor: Adrián Baeza

Fecha: 01/02/2023
"""

from typeguard import typechecked


@typechecked
class Punto:

    def __init__(self, x: int = 0, y: int = 0):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: int):
        self.__y = value

    def invertir(self):
        self.__x, self.__y = self.__y, self.__x

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__x}, {self.__y})"
