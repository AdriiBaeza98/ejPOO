"""
Propósito: crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera.
Para la clase Vehicle, crea los atributos de clase vehicles_created y total_kilometers,
así como el atributo de instancia kilometers_traveled.

En la clase Vehicle, crea un método para viajar (travel) que incremente los kilómetros recorridos.
En la clase Bike haz un método para hacer el caballito y en la clase Car otro para quemar rueda.

Autor: Adrián Baeza

Fecha: 22/02/2023
"""
from abc import ABC
from typeguard import typechecked


@typechecked
class Vehiculo(ABC):
    __vehiculos_creados = 0  # Atributos de clase
    __kilometros_totales = 0

    def __init__(self):
        self.__kilometros_recorridos = 0  # Atributo de instancia
        Vehiculo.__vehiculos_creados += 1

    @property
    def kilometros_recorridos(self):
        return self.__kilometros_recorridos

    @classmethod
    def vehiculos_creados(cls):
        return cls.__vehiculos_creados

    @classmethod
    def kilometros_totales(cls):
        return cls.__kilometros_totales

    def viajar(self, kilometros: int):
        if kilometros < 0:
            raise ValueError("Los kilómetros recorridos no pueden ser negativos")
        self.__kilometros_recorridos += kilometros
        Vehiculo.__kilometros_totales += kilometros

    def __repr__(self):
        return f"{self.__class__.__name__}(kilometraje={self.__kilometros_recorridos})"


class Bicicleta(Vehiculo):

    def __init__(self):
        super().__init__()
        self.__caballito = "¡Haciendo caballito!"

    def hacer_caballito(self):
        print(self.__caballito)


class Coche(Vehiculo):

    def __init__(self):
        super().__init__()
        self.__quemar_rueda = "¡Quemando rueda!"

    def quemar_rueda(self):
        print(self.__quemar_rueda)
