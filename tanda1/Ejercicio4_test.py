"""
Prueba del objeto Dado ejercicio 4.
Implementa un tester que tenga un vector de 4 dados y los lance una serie de veces.
"""
import random
from Ejercicio4 import Dado

print("Prueba del ejercicio 4 (objeto Dado)")
print("------------------------------------\n")

NUM_DADOS = 4
NUM_LANZAMIENTOS = random.randint(3, 10)

dados = []

for i in range(NUM_DADOS):
    dados.append(Dado())

for i in range(NUM_LANZAMIENTOS):
    print(f"Tirada {i + 1}")
    print("--------")
    print([dado.lanzar() for dado in dados])
    print()
