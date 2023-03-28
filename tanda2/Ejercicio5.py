"""
Propósito: Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

- Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
- Obtener el número de elementos almacenados (tamaño).
- Saber si la pila o la cola está vacía.
- Vaciar completamente la pila o la cola.

Para el caso de la pila:
- Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
- Desapilar (pop): se saca (debe devolverse) el elemento superior de la pila y se elimina.
- Leer el elemento superior de la pila sin retirarlo (top).

Para el caso de la cola:
- Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
- Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir,
el primer elemento que entró.
- Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

Autor: Adrián Baeza

Fecha: 09/02/2023
"""

from typeguard import typechecked


@typechecked
class Pila:

    def __init__(self, *elementos):
        self.__pila = []
        for elemento in elementos:
            self.__pila.append(elemento)

    @classmethod
    def desde_pila(cls, otra: 'Pila'):
        nueva_pila = cls()
        nueva_pila.__pila = list(otra.__pila)
        return nueva_pila

    @property
    def tamanno(self):
        return len(self.__pila)

    def esta_vacia(self):
        if not self.__pila:
            return True
        else:
            return False

    def vaciar(self):
        self.__pila = []

    def apilar(self, elemento):
        self.__pila = [elemento] + self.__pila  # También podría ser con insert --> self.__pila.insert(0, elemento)

    def desapilar(self):
        return self.__pila.pop(0)

    def superior(self):
        return self.__pila[0]

    def __str__(self):
        return str(self.__pila)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__pila})"


class Cola:

    def __init__(self, *elementos):
        self.__cola = []
        for elemento in elementos:
            self.__cola.append(elemento)

    @classmethod
    def desde_cola(cls, otra: 'Cola'):
        nueva_cola = cls()
        nueva_cola.__pila = list(otra.__cola)
        return nueva_cola

    @property
    def tamanno(self):
        return len(self.__cola)

    def esta_vacia(self):
        if not self.__cola:
            return True
        else:
            return False

    def vaciar(self):
        self.__cola = []

    def encolar(self, elemento):
        self.__cola = self.__cola + [elemento]

    def desencolar(self):
        return self.__cola.pop(0)

    def frontal(self):
        return self.__cola[0]

    def __str__(self):
        return str(self.__cola)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__cola})"
