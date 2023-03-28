"""
Implementa un test donde crees un punto, lo imprimas utilizando de manera implícita el método __str__(),
imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a imprimir el punto.
"""

from Ejercicio2 import Punto

print("Prueba del ejercicio 2 (objeto Punto)")
print("-------------------------------------\n")

p = Punto(4, 9)
print(f"Punto {p}")
print(f"Coordenada x del punto: {p.x}")
p.x = 0
print(f"Resultado del punto modificado: {p}")
p.invertir()
print(f"Resultado del nuevo punto invertido: {p}")
