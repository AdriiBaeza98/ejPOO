"""
Prueba de pila y cola ejercicio 5
"""

from Ejercicio5 import Pila, Cola

print("Prueba del ejercicio 5 (objetos Pila y Cola)")
print("--------------------------------------------\n")
print("---------------")
print("Pila de enteros")
print("---------------\n")

p1 = Pila(1, 2, 3, 4, 5)

print(f"Contenido de la pila: {p1}\n")
print(f"Elemento desapilado: {p1.desapilar()}\n")
elemento_pila = int(input("Introduce un nuevo elemento (entero) a apilar: "))
p1.apilar(elemento_pila)
print(f"\nContenido final de la pila: {p1}\n")

print("---------------")
print("Cola de nombres")
print("---------------\n")

c1 = Cola("Pepe", "Juan", "Ana")

print(f"Contenido de la cola: {c1}\n")
print(f"Elemento desencolado: {c1.desencolar()}")
elemento_cola = str(input("Introduce un nuevo elemento a apilar: "))
c1.encolar(elemento_cola)
print(f"\nContenido final de la cola: {c1}\n")
