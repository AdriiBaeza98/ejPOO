"""
Propósito: Crear un menú con una clase a la que llamaremos Menú, esta clase permitirá ir añadiendo opciones
y escoger alguna opción.

Autor: Adrián Baeza

Fecha: 14/02/2023
"""

from typeguard import typechecked


@typechecked
class Menu:

    def __init__(self, titulo: str, *opciones: str):
        self.__titulo = str(titulo)
        self.__opciones = []
        for opcion in opciones:
            self.__opciones.append(opcion)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def opciones(self):
        return self.__opciones

    def mostrar(self):
        print(f"{self.__titulo}")
        print("-" * len(self.__titulo))
        for n in range(len(self.__opciones)):
            print(f"{n + 1}. {self.__opciones[n]}")

    def elegir_opcion(self):
        numero = int(input("\nElige una opción: "))
        if not 1 <= numero <= len(self.__opciones):
            raise ValueError(f"El número escogido no se encuentra en el rango de opciones. Recibido: {numero}")
        return numero

    def __str__(self):
        return self.__titulo

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__titulo})"
