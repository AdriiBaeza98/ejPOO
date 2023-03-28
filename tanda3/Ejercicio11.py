"""
Propósito: implementa la clase Terminal. Un terminal tiene asociado un número de teléfono.
Los terminales se pueden llamar unos a otros y el tiempo de conversación corre para ambos. Los números
de teléfono tienen que validarse como tales al crear el objeto (solo dígitos, empiezan por 9, 6 ó 7,
su longitud es de nueve dígitos) y no puede haber dos terminales con el mismo número.

Autor: Adrián Baeza

Fecha: 23/02/2023
"""
from typeguard import typechecked


@typechecked
class Terminal:
    __nums_telf = []

    def __init__(self, numero: str):
        if not numero.isdigit() or len(numero) != 9 or numero[0] not in ["9", "6", "7"]:
            raise ValueError("El número introducido no es válido")
        if numero in Terminal.__nums_telf:
            raise ValueError("No puede haber dos terminales con el mismo número")
        Terminal.__nums_telf.append(numero)
        self.__telf = numero
        self.__tiempo = 0

    @property
    def telf(self):
        return self.__telf[:3] + " " + self.__telf[3:5] + " " + self.__telf[5:7] + " " + self.__telf[7:9]

    def llamar(self, terminal: 'Terminal', segundos: int):
        if self.__telf == terminal.telf:
            raise ValueError("El terminal no puede llamarse a sí mismo")
        if segundos < 0:
            raise ValueError("Los segundos de llamada no pueden ser negativos")
        self.__tiempo += segundos
        terminal.__tiempo += segundos

    def __str__(self):
        return f"Nº {self.telf} - {self.__tiempo}s de conversación"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__telf})"
