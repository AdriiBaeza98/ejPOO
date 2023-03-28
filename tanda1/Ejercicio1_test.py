"""
Test del ejercicio 1
"""

from Ejercicio1 import Dado

print("Prueba del ejercicio 1 (objeto Dado)")
print("------------------------------------")

dado = Dado()

print(f"Valor inicial: {dado}\n")

for i in range(3):
    dado.lanzar()
    print(f"Tirada {i + 1}: {dado}")
