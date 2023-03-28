"""
Propósito: Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son
intervalos de tiempo y se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

- Sumar y restar objetos de la clase (el resultado es otro objeto).
- Sumar y restar segundos, minutos u horas (se cambia el objeto actual).
- Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

Autor: Adrián Baeza

Fecha: 13/02/2023
"""

from typeguard import typechecked


@typechecked
class Duracion:

    def __init__(self, horas, minutos=None, segundos=None):
        if isinstance(horas, Duracion) and (minutos, segundos) == (None, None):
            otra_duracion = horas
            self.__horas = otra_duracion.horas
            self.__minutos = otra_duracion.minutos
            self.__segundos = otra_duracion.segundos
        elif isinstance(horas, int) and isinstance(minutos, int) and isinstance(segundos, int):
            self.__horas = horas
            self.__minutos = minutos
            self.__segundos = segundos
            self.__normalizar()
        else:
            raise TypeError("El objeto Duracion sólo puede construirse con tres enteros o con otro objeto Duracion")

    def __normalizar(self):
        while self.__segundos >= 60:
            self.__minutos += 1
            self.__segundos -= 60
        while self.__minutos >= 60:
            self.__horas += 1
            self.__minutos -= 60
        while self.__segundos < 0:
            self.__minutos -= 1
            self.__segundos += 60
        while self.__minutos < 0:
            self.__horas -= 1
            self.__minutos += 60
        if self.__horas < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, value):
        nueva_duracion = Duracion(value, self.minutos, self.segundos)
        self.__horas = nueva_duracion.horas
        self.__minutos = nueva_duracion.minutos
        self.__segundos = nueva_duracion.segundos

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, value):
        nueva_duracion = Duracion(self.horas, value, self.segundos)
        self.__horas = nueva_duracion.horas
        self.__minutos = nueva_duracion.minutos
        self.__segundos = nueva_duracion.segundos

    @property
    def segundos(self):
        return self.__segundos

    @segundos.setter
    def segundos(self, value):
        nueva_duracion = Duracion(self.horas, self.minutos, value)
        self.__horas = nueva_duracion.horas
        self.__minutos = nueva_duracion.minutos
        self.__segundos = nueva_duracion.segundos

    def sumar_segundos(self, segundos: int):
        self.segundos += segundos

    def restar_segundos(self, segundos: int):
        self.segundos -= segundos

    def sumar_minutos(self, minutos: int):
        self.minutos += minutos

    def restar_minutos(self, minutos: int):
        self.minutos -= minutos

    def sumar_horas(self, horas: int):
        self.horas += horas

    def restar_horas(self, horas: int):
        self.horas -= horas

    def __add__(self, tiempo: 'Duracion'):
        nueva_duracion = Duracion(tiempo)
        nueva_duracion.horas = self.__horas + tiempo.horas
        nueva_duracion.minutos = self.__minutos + tiempo.minutos
        nueva_duracion.segundos = self.__segundos + tiempo.segundos
        return Duracion(nueva_duracion)

    def __sub__(self, tiempo: 'Duracion'):
        nueva_duracion = Duracion(tiempo)
        nueva_duracion.horas = self.__horas - tiempo.horas
        nueva_duracion.minutos = self.__minutos - tiempo.minutos
        nueva_duracion.segundos = self.__segundos - tiempo.segundos
        return Duracion(nueva_duracion)

    def __str__(self):
        return f"{self.__horas:02d}h {self.__minutos:02d}m {self.__segundos:02d}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__horas}, {self.__minutos}, {self.__segundos})"
