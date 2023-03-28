"""
Implementa un test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre
el área y perímetro de dicho rectángulo.
"""

from Ejercicio2 import Punto
from Ejercicio3 import Rectangulo

print("Prueba del ejercicio 3 (objeto Rectángulo)")
print("------------------------------------------\n")

p1 = Punto(3, 2)
p2 = Punto(5, 4)

r = Rectangulo(p1, p2)

print(f"El perímetro del {r} es {r.perimetro} cm")
print(f"El área del {r} es {r.area} cm²")
