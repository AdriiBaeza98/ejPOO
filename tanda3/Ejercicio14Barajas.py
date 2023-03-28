"""
Propósito: crea las clases Baraja Española e Inglesa (SpanishDeck e EnglishDeck) que heredan de Deck.

Autor: Adrián Baeza

Fecha: 28/02/2023
"""

from Ejercicio14Carta import Carta
from Ejercicio14Baraja import Baraja


class BarajaEspannola(Baraja):

    def __init__(self):
        numeros = "1 2 3 4 5 6 7 8 9 SOTA CABALLO REY".split()
        palos = "OROS COPAS ESPADAS BASTOS".split()
        cartas = [Carta(n, p) for p in palos for n in numeros]
        super().__init__(cartas)


class BarajaInglesa(Baraja):

    def __init__(self):
        numeros = "1 2 3 4 5 6 7 8 9 10 J Q K".split()
        palos = "♠ ♡ ♢ ♣".split()
        cartas = [Carta(n, p) for p in palos for n in numeros]
        super().__init__(cartas)
