"""
Prueba de la clase Terminal ejercicio 11.

A continuación se proporciona el contenido del programa principal que usa esta clase y el resultado
que debe aparecer por pantalla.

Programa principal:

t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.call(t2, 320)
t1.call(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)

Salida:

No 678 11 22 33 - 0s de conversación
No 644 74 44 69 - 0s de conversación
No 678 11 22 33 - 520s de conversación
No 644 74 44 69 - 320s de conversación
No 622 32 89 09 - 200s de conversación
No 664 73 98 18 - 0s de conversación
"""
from Ejercicio11 import Terminal

t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.llamar(t2, 320)
t1.llamar(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)
