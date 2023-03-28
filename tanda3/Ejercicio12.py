"""
Propósito: implementa la clase Mobile como subclase de Terminal (la clase del ejercicio anterior que ya
no hace falta modificar). Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes
controlar esto). El coste por minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos.
La tarifa se puede cambiar. Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe
la llamada. El total tarificado debe aparecer con dos decimales.

Autor: Adrián Baeza

Fecha: 23/02/2023
"""
from typeguard import typechecked
from Ejercicio11 import Terminal


@typechecked
class Movil(Terminal):
    __tarifas = ["RATA", "MONO", "BISONTE"]
    __precios = [0.06, 0.12, 0.30]

    def __init__(self, numero: str, tarifa: str):
        if not tarifa.upper() in Movil.__tarifas:
            raise ValueError("La tarifa introducida no existe")
        super().__init__(numero)
        self.__tarifa = tarifa.upper()
        self.__precio = 0

    @property
    def tarifa(self):
        return self.__tarifa

    @property
    def precio(self):
        return self.__precio

    def llamar(self, terminal: 'Terminal', segundos: int):
        super().llamar(terminal, segundos)
        for n in range(len(Movil.__tarifas)):
            if self.__tarifa == Movil.__tarifas[n]:
                self.__precio += (segundos / 60) * Movil.__precios[n]

    def __str__(self):
        return super().__str__() + f" - tarificados {self.__precio:.2f} euros"
