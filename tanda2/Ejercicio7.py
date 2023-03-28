"""
Propósito: Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador)
de forma que podamos hacer las siguientes operaciones:

- Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción
se construye simplificada, no se puede dividir por cero.
- Obtener resultado de la fracción (número real).
- Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
- Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).

Autor: Adrián Baeza

Fecha: 14/02/2023
"""

import math
from typeguard import typechecked


@typechecked
class Fraccion:

    def __init__(self, numerador: int, denominador: int):
        if denominador == 0:
            raise ZeroDivisionError("La fracción no puede tener un denominador igual a 0, ya que un número no se "
                                    "puede dividir por 0")
        mcd = math.gcd(numerador, denominador)
        self.__numerador = numerador // mcd
        self.__denominador = denominador // mcd

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    def resultado(self):
        return self.__numerador / self.__denominador

    def __mul__(self, numero: (int, 'Fraccion')):
        if isinstance(numero, int):
            return Fraccion(self.__numerador * numero, self.__denominador)
        return Fraccion(self.__numerador * numero.numerador, self.__denominador * numero.denominador)

    def __rmul__(self, numero):
        return self * numero

    def __truediv__(self, fraccion: 'Fraccion'):
        return Fraccion(self.__numerador * fraccion.denominador, self.__denominador * fraccion.numerador)

    def __add__(self, fraccion: 'Fraccion'):
        if self.__.denominador == fraccion.denominador:
            return Fraccion(self.__numerador + fraccion.numerador, self.__denominador)
        else:
            fraccion1_convertida = Fraccion(self.numerador, self.denominador)  # Variables para no modificar las
            # fracciones
            fraccion2_convertida = Fraccion(fraccion.numerador, fraccion.denominador)
            mcm = math.lcm(self.denominador, fraccion.denominador)
            fraccion1_convertida.__numerador = self.numerador * (mcm // self.denominador)
            fraccion1_convertida.__denominador = mcm
            fraccion2_convertida.__numerador = fraccion.numerador * (mcm // fraccion.denominador)
            fraccion2_convertida.__denominador = mcm
            fraccion1_convertida.__numerador = fraccion1_convertida.__numerador + fraccion2_convertida.__numerador
            # Fracción resultado, que guardamos en la convertida, ya que no la vamos a necesitar
            return Fraccion(fraccion1_convertida.numerador, fraccion1_convertida.denominador)

    def __neg__(self):
        return Fraccion(self.__numerador * -1, self.__denominador * -1)

    def __sub__(self, fraccion: 'Fraccion'):
        if self.__denominador == fraccion.denominador:
            return Fraccion(self.__numerador - fraccion.numerador, self.__denominador)
        else:
            fraccion1_convertida = Fraccion(self.numerador, self.denominador)  # Variables para no modificar las
            # fracciones
            fraccion2_convertida = Fraccion(fraccion.numerador, fraccion.denominador)
            mcm = math.lcm(self.denominador, fraccion.denominador)
            fraccion1_convertida.__numerador = self.numerador * (mcm // self.denominador)
            fraccion1_convertida.__denominador = mcm
            fraccion2_convertida.__numerador = fraccion.numerador * (mcm // fraccion.denominador)
            fraccion2_convertida.__denominador = mcm
            fraccion1_convertida.__numerador = fraccion1_convertida.__numerador - fraccion2_convertida.__numerador
            # Fracción resultado, que guardamos en la convertida, ya que no la vamos a necesitar
            return Fraccion(fraccion1_convertida.numerador, fraccion1_convertida.denominador)

    def __str__(self):
        return f"{self.__numerador} / {self.__denominador}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerador}, {self.__denominador})"
