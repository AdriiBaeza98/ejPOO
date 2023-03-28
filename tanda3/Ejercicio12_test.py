"""
Prueba de la clase Movil ejercicio 12.

A continuación se proporciona el contenido del programa principal que usa esta clase y el resultado
que debe aparecer por pantalla.

Programa principal:

m1 = Mobile("678112233", "rata")
m2 = Mobile("644744469", "mono")
m3 = Mobile("622328909", "bisonte")
print(m1)
print(m2)
m1.call(m2, 320)
m1.call(m3, 200)
m2.call(m3, 550)
print(m1)
print(m2)
print(m3)

Salida:

Nº 678 11 22 33 - 0s de conversación - tarificados 0,00 euros
Nº 644 74 44 69 - 0s de conversación - tarificados 0,00 euros
Nº 678 11 22 33 - 520s de conversación - tarificados 0,52 euros
Nº 644 74 44 69 - 870s de conversación - tarificados 1,10 euros
Nº 622 32 89 09 - 750s de conversación - tarificados 0,00 euros
"""
from Ejercicio12 import Movil

m1 = Movil("678112233", "rata")
m2 = Movil("644744469", "mono")
m3 = Movil("622328909", "bisonte")
print(m1)
print(m2)
m1.llamar(m2, 320)
m1.llamar(m3, 200)
m2.llamar(m3, 550)
print(m1)
print(m2)
print(m3)
