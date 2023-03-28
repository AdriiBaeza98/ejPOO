"""
Propósito: implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos.
El número de cuenta se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos
con el mismo número de cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo,
se pondrá a cero inicialmente. En una cuenta se pueden hacer ingresos y gastos. También es posible hacer
una transferencia entre una cuenta y otra. No se permite el saldo negativo.

Autor: Adrián Baeza

Fecha: 27/02/2023
"""
import random
from typeguard import typechecked


@typechecked
class CuentaBanco:
    __nums_cuenta = []

    def __init__(self, saldo: float = 0):
        if saldo < 0:
            raise ValueError("El saldo de una cuenta no puede ser negativo")
        self.__saldo = saldo
        self.__numero_cuenta = CuentaBanco.__crear_numero_cuenta()

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @classmethod
    def __crear_numero_cuenta(cls):
        while True:
            numero = random.randint(1000000000, 9999999999)
            if numero not in cls.__nums_cuenta:
                break
        cls.__nums_cuenta.append(numero)
        return numero

    def ingresar(self, dinero: float):
        if dinero < 0:
            raise ValueError("No se pueden ingresar cantidades negativas")
        self.__saldo += dinero

    def retirar(self, dinero: float):
        if dinero < 0:
            raise ValueError("No se pueden retirar cantidades negativas")
        if dinero > self.__saldo:
            raise ValueError("No se puede retirar una cantidad mayor al saldo de la cuenta")
        self.__saldo -= dinero

    def transferir(self, cuenta: 'CuentaBanco', dinero: float):
        if dinero < 0:
            raise ValueError("No se pueden transferir cantidades negativas")
        if dinero > self.__saldo:
            raise ValueError("No se puede transferir una cantidad mayor al saldo de la cuenta")
        self.__saldo -= dinero
        cuenta.__saldo += dinero

    def __str__(self):
        return f"Número de cta: {self.__numero_cuenta} Saldo: {self.__saldo:.2f} €"
