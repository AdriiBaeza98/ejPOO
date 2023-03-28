"""
Propósito: probar la clase Menú con las siguientes opciones:
- Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa.
Si no se introduce correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
- Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.
Si el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida
(se ha ejecutado la opción anterior), si no la hay mostrará un mensaje de error.
- Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
- Añadir años a la fecha. El mismo procedimiento que la opción 2.
- Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no
lo es da error) y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior,
igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.
- Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
- Terminar.

Consideraciones a tener en cuenta:
- Las fechas las manejaremos con la clase datetime.date.
"""

import datetime
from dateutil.relativedelta import relativedelta
from Ejercicio8 import Menu
import locale
locale.setlocale(locale.LC_ALL, 'es-ES')

fecha = datetime.date.today()


def main():
    m1 = Menu("Gestión de fecha", "Introducir fecha", "Añadir días a la fecha", "Añadir meses a la fecha",
              "Añadir años a la fecha", "Comparar con otra fecha", "Mostrar fecha en formato largo",
              "Terminar")

    datos_introducidos = False
    while True:
        print("")
        m1.mostrar()
        numero = m1.elegir_opcion()
        if not datos_introducidos and numero != 1 and numero != 7:
            print("\nERROR: primero debe introducirse una fecha (primera opción)")
            continue
        if numero == 1:
            introducir_fecha()
            datos_introducidos = True
            continue
        if numero == 2:
            sumar_dias()
            continue
        if numero == 3:
            sumar_meses()
            continue
        if numero == 4:
            sumar_annos()
            continue
        if numero == 5:
            comparar()
            continue
        if numero == 6:
            mostrar_fecha()
            continue
        else:
            terminar()


def introducir_fecha():
    global fecha
    while True:
        fecha = input("Introduce una fecha(formato dd/mm/aaaa): ")
        if len(fecha) != 10 or fecha[2] != "/" and fecha[5] != "/":
            print("\nERROR: el formato de fecha introducido no es válido. Inténtalo de nuevo\n")
        else:
            break
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    anno = int(fecha[6:10])
    fecha = datetime.date(anno, mes, dia)


def sumar_dias():
    global fecha
    dias = int(input("Introduce los días a añadir: "))
    fecha += datetime.timedelta(days=dias)


def sumar_meses():
    global fecha
    meses = int(input("Introduce los meses a añadir: "))
    fecha += relativedelta(months=meses)


def sumar_annos():
    global fecha
    annos = int(input("Introduce los meses a añadir: "))
    fecha += relativedelta(years=annos)


def comparar():
    global fecha
    while True:
        fecha2 = input("Introduce una nueva fecha para comparar(formato dd/mm/aaaa): ")
        if len(fecha2) != 10 or fecha2[2] != "/" and fecha2[5] != "/":
            print("\nERROR: el formato de fecha introducido no es válido. Inténtalo de nuevo\n")
        else:
            break
    dia = int(fecha2[0:2])
    mes = int(fecha2[3:5])
    anno = int(fecha2[6:10])
    fecha2 = datetime.date(anno, mes, dia)
    if fecha2 < fecha:
        print("\nLa fecha introducida es menor que la fecha original")
    if fecha2 > fecha:
        print("\nLa fecha introducida es mayor que la fecha original")
    if fecha2 == fecha:
        print("\nLa fecha introducida es igual que la fecha original")


def mostrar_fecha():
    global fecha
    print(fecha.strftime("%A, %d de %B del %Y"))


def terminar():
    print("\nEl programa ha terminado")
    exit(0)


if __name__ == '__main__':
    main()
