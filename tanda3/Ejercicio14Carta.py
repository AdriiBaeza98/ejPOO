"""
Propósito: crea la clase Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos)
y un valor (de un conjunto de valores).

Autor: Adrián Baeza

Fecha: 28/02/2023
"""

from dataclasses import dataclass
from typeguard import typechecked


@typechecked
@dataclass(frozen=True)
class Carta:
    numero: str
    palo: str
