"""
Prueba de la clase Vehiculo y subclases Coche y Bicicleta del ejercicio 10

Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior)
como el que se muestra a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Ver kilometraje de la bicicleta
6. Ver kilometraje del coche
7. Ver kilometraje total
8. Salir

Elige una opción (1-8):

"""

from EjerciciosPOO.tanda2.Ejercicio8 import Menu
from Ejercicio10 import Vehiculo, Coche, Bicicleta

mi_bici = Bicicleta()
mi_coche = Coche()
m1 = Menu("VEHÍCULOS", "Anda con la bicicleta", "Haz el caballito con la bicicleta", "Anda con el coche",
          "Quema rueda con el coche", "Ver kilometraje de la bicicleta", "Ver kilometraje del coche",
          "Ver kilometraje total", "Salir")

while True:
    print("")
    m1.mostrar()
    numero = m1.elegir_opcion()
    match numero:
        case 1:
            kilometros = int(input("Introduce los kilómetros recorridos con la bicicleta: "))
            mi_bici.viajar(kilometros)
        case 2:
            mi_bici.hacer_caballito()
        case 3:
            kilometros = int(input("Introduce los kilómetros recorridos con el coche: "))
            mi_coche.viajar(kilometros)
        case 4:
            mi_coche.quemar_rueda()
        case 5:
            print(f"La bicicleta lleva {mi_bici.kilometros_recorridos} km")
        case 6:
            print(f"El coche lleva {mi_coche.kilometros_recorridos} km")
        case 7:
            print(f"Los vehículos han recorrido {Vehiculo.kilometros_totales()} km en total")
        case 8:
            break
print("\nEl programa ha terminado")
