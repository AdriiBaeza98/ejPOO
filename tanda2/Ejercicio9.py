"""
Propósito: nos hemos enterado de que la clase datetime.date ha sido comprometida y tenemos que crear una
clase nueva para almacenar fechas locales (Date), en este caso la clase será mutable (los objetos pueden
cambiar el día, mes o año). Los objetos de la clase Fecha son fechas de tiempo y se crean de la forma:

f1 = Date(1, 10, 2020)  # almacena el 1 de octubre de 2020
f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Crea métodos para:

- Sumar y restar días a la fecha.
- Restar fechas. Devuelve el número de días comprendidos entre ambas.
- Comparar la fecha almacenada con otra.
- Saber si el año de la fecha almacenada es bisiesto.
- Obtener el día de la semana de una fecha concreta.
- El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

Autor: Adrián Baeza

Fecha: 20/02/2023
"""

from typeguard import typechecked


@typechecked
class Fecha:

    def __init__(self, dia, mes=None, anno=None):
        if isinstance(dia, Fecha) and (mes, anno) == (None, None):
            otra_fecha = dia
            self.__dia = otra_fecha.dia
            self.__mes = otra_fecha.mes
            self.__anno = otra_fecha.anno
        elif isinstance(dia, int) and isinstance(mes, int) and isinstance(anno, int):
            self.__comprobar_fecha(dia, mes, anno)
            self.__dia = dia
            self.__mes = mes
            self.__anno = anno
        else:
            raise TypeError("El objeto Fecha sólo puede construirse con tres enteros o con otro objeto Fecha")

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        self.__comprobar_fecha(value, self.__mes, self.__anno)
        self.__dia = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        self.__comprobar_fecha(self.__dia, value, self.__anno)
        self.__mes = value

    @property
    def anno(self):
        return self.__anno

    @anno.setter
    def anno(self, value):
        self.__comprobar_fecha(self.__dia, self.__mes, value)
        self.__anno = value

    @staticmethod
    def __comprobar_fecha(dia: int, mes: int, anno: int):
        if dia < 1 or dia > 31 or mes in [4, 6, 9, 11] and dia > 30:
            raise ValueError("La fecha introducida es incorrecta")
        if mes < 1 or mes > 12:
            raise ValueError("La fecha introducida es incorrecta")
        if mes == 2:
            if Fecha.__es_bisiesto(anno) and dia > 29:
                raise ValueError("La fecha introducida es incorrecta")
            elif dia > 28:
                raise ValueError("La fecha introducida es incorrecta")
        if anno < 1:
            raise ValueError("La fecha introducida es incorrecta")

    @staticmethod
    def __dias_mes(mes: int, anno: int):
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.__es_bisiesto(anno):
            dias_mes[1] = 29
        return dias_mes[mes - 1]

    @staticmethod
    def __nombre_mes(mes: int):
        nombre_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                      "Octubre", "Noviembre", "Diciembre"]
        return nombre_mes[mes - 1]

    @staticmethod
    def __es_bisiesto(anno: int):
        if anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0):
            return True
        return False

    def sumar_dias(self, dias: int):
        if dias < 0:
            raise ValueError("No se pueden sumar valores negativos")
        self.__dia += dias
        while self.__dia > self.__dias_mes(self.__mes, self.__anno):
            self.__dia -= self.__dias_mes(self.__mes, self.__anno)
            self.__mes += 1
            if self.__mes > 12:
                self.__mes -= 12
                self.__anno += 1

    def restar_dias(self, dias: int):
        if dias < 0:
            raise ValueError("No se pueden restar valores negativos")
        self.__dia -= dias
        while self.__dia < 1:
            self.__mes -= 1
            if self.__mes == 0:
                self.__dia += self.__dias_mes(12, self.__anno)
                self.__mes += 12
                self.__anno -= 1
            else:
                self.__dia += self.__dias_mes(self.__mes, self.__anno)

    def __restar_fecha(self, fecha: 'Fecha'):
        if self < fecha:
            fecha1, fecha2 = Fecha(self), Fecha(fecha)
            signo = -1
        else:
            fecha1, fecha2 = Fecha(fecha), Fecha(self)
            signo = 1
        # Operandos para averiguar el número de días comprendidos entre las dos fechas
        dias_fecha1 = Fecha.__dias_mes(fecha1.mes, fecha1.anno) - fecha1.dia
        dias_meses = 0
        dias_fecha2 = fecha2.dia
        resultado = 0
        if fecha1.anno == fecha2.anno:
            if fecha1.mes == fecha2.mes:
                if fecha1.dia < fecha2.dia:
                    resultado = fecha2.dia - fecha1.dia
            else:
                fecha1.mes += 1
                while fecha1.mes < fecha2.mes:
                    dias_meses += Fecha.__dias_mes(fecha1.mes, fecha1.anno)
                    fecha1.mes += 1
                resultado = dias_fecha1 + dias_meses + dias_fecha2
        else:
            while fecha1.mes < 12:  # Sumamos los días restantes hasta el final de ese mismo año
                fecha1.mes += 1
                dias_meses += Fecha.__dias_mes(fecha1.mes, fecha1.anno)
            fecha1.mes = 1
            fecha1.anno += 1
            while fecha1.anno < fecha2.anno:  # Sumamos los días comprendidos entre los años completos de ambas fechas
                if Fecha.__es_bisiesto(fecha1.anno):
                    dias_meses += 366
                else:
                    dias_meses += 365
                fecha1.anno += 1
            fecha2.mes -= 1
            while fecha2.mes >= 1:  # Sumamos los días comprendidos entre el inicio de año y la fecha
                dias_meses += Fecha.__dias_mes(fecha2.mes, fecha2.anno)
                fecha2.mes -= 1
            resultado = dias_fecha1 + dias_meses + dias_fecha2
        return signo * resultado

    """def __restar_fecha(self, fecha: 'Fecha'):  # Tarda mucho en ejecutarse
        if self < fecha:
            fecha1, fecha2 = self, fecha
            signo = -1
        else:
            fecha1, fecha2 = fecha, self
            signo = 1
        dias = 0
        while fecha1 < fecha2:
            fecha1 += 1
            dias += 1
        return signo * dias"""

    def formato_iso(self):  # Este paso de la fecha a formato cadena permite la comparación entre objetos
        return f"{self.__anno:04d}-{self.__mes:04d}-{self.__dia:04d}"

    def dia_semana(self):
        dia_semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        modulo_mes = 0  # Necesario para la fórmula posterior
        for mes in range(self.__mes - 1):
            modulo_mes += self.__dias_mes(mes + 1, self.__anno) % 7
        modulo_mes %= 7
        dia = ((self.__anno - 1) % 7 + ((self.__anno - 1) // 4 - (3 * ((self.__anno - 1) // 100 + 1) // 4)) % 7
               + modulo_mes + self.__dia % 7) % 7  # Fórmula para calcular el día de la semana
        return dia_semana[dia]

    """def dia_semana(self):  # Tarda mucho en ejecutarse
        dias_totales = self - self.__class__(1, 1, 1)  # ese día fue lunes
        dia_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        return dia_semana[dias_totales % 7]"""

    # En este caso, la sobrecarga sólo permite sumar enteros (no objetos tipo Fecha)
    def __add__(self, dias: int):
        if dias < 0:
            raise ValueError("No se pueden sumar valores negativos")
        nueva_fecha = Fecha(self)
        nueva_fecha.sumar_dias(dias)
        return Fecha(nueva_fecha)

    def __sub__(self, dias: (int, 'Fecha')):
        if isinstance(dias, Fecha):
            return self.__restar_fecha(dias)
        if dias < 0:
            raise ValueError("No se pueden restar valores negativos")
        nueva_fecha = Fecha(self)
        nueva_fecha.restar_dias(dias)
        return Fecha(nueva_fecha)

    def __radd__(self, n: int):
        return self + n

    def __eq__(self, fecha: 'Fecha'):
        return (self.__dia, self.__mes, self.__anno) == (fecha.__dia, fecha.__mes, fecha.__anno)

    def __ne__(self, fecha: 'Fecha'):
        return not self == fecha

    def __gt__(self, fecha: 'Fecha'):
        return self.formato_iso() > fecha.formato_iso()

    def __ge__(self, fecha: 'Fecha'):
        return self > fecha or self == fecha

    def __lt__(self, fecha: 'Fecha'):
        return not self >= fecha

    def __le__(self, fecha: 'Fecha'):
        return not self > fecha

    def __str__(self):
        return f"{self.__dia} de {self.__nombre_mes(self.__mes)} del {self.__anno}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dia}, {self.__mes}, {self.__anno})"
