# -------------------------------------------------------------
# ACTIVIDAD 1 - SEMANA 3
# ROBUSTEZ CON ENCAPSULAMIENTO, HERENCIA Y POLIMORFISMO
# Quantum Core
# -------------------------------------------------------------

import os


# -------------------------------------------------------------
# CLASE BASE
# -------------------------------------------------------------

class TransaccionBase:

    def __init__(self, cliente_id, tipo, monto):

        self._cliente_id = cliente_id
        self._tipo = tipo
        self._monto = 0

        self.monto = monto

    # Getter cliente_id
    @property
    def cliente_id(self):
        return self._cliente_id

    # Setter cliente_id
    @cliente_id.setter
    def cliente_id(self, nuevo_cliente):
        self._cliente_id = nuevo_cliente

    # Getter tipo
    @property
    def tipo(self):
        return self._tipo

    # Setter tipo
    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    # Getter monto
    @property
    def monto(self):
        return self._monto

    # Setter monto
    @monto.setter
    def monto(self, nuevo_monto):

        if nuevo_monto < 0:
            raise ValueError("El monto no puede ser negativo.")

        self._monto = nuevo_monto

    # Método para calcular el impacto
    def calcular_impacto(self):
        return 0

    # Método para mostrar la información
    def obtener_informacion(self):
        return (
            f"Cliente: {self.cliente_id}, "
            f"Tipo: {self.tipo}, "
            f"Monto: {self.monto}, "
            f"Impacto: {self.calcular_impacto()}"
        )


# -------------------------------------------------------------
# CLASE HIJA - CREDITO
# -------------------------------------------------------------

class TransaccionCredito(TransaccionBase):

    def calcular_impacto(self):
        return self.monto * 0.05


# -------------------------------------------------------------
# CLASE HIJA - DEBITO
# -------------------------------------------------------------

class TransaccionDebito(TransaccionBase):

    def calcular_impacto(self):
        return 10000


# -------------------------------------------------------------
# LEER Y ALMACENAR LOS DATOS
# -------------------------------------------------------------

def leer_y_almacenar_datos(nombre_archivo):

    lista_transacciones = []

    with open(nombre_archivo, "r") as archivo:

        for linea in archivo:

            partes = linea.strip().split(",")

            if len(partes) == 3:

                cliente_id = partes[0].strip()
                tipo = partes[1].strip()
                monto = int(partes[2].strip())

                if tipo == "CREDITO":

                    transaccion = TransaccionCredito(
                        cliente_id,
                        tipo,
                        monto
                    )

                elif tipo == "DEBITO":

                    transaccion = TransaccionDebito(
                        cliente_id,
                        tipo,
                        monto
                    )

                lista_transacciones.append(transaccion)

    return lista_transacciones


# -------------------------------------------------------------
# CALCULAR MONTO TOTAL
# -------------------------------------------------------------

def calcular_monto_total(lista_transacciones):

    total = 0

    for transaccion in lista_transacciones:

        total = total + transaccion.monto

    return total


# -------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# -------------------------------------------------------------

def ejecutar_sistema():

    carpeta_actual = os.path.dirname(__file__)

    nombre_archivo = os.path.join(
        carpeta_actual,
        "transacciones.txt"
    )

    lista_transacciones = leer_y_almacenar_datos(nombre_archivo)

    print("--- TRANSACCIONES ---")

    for transaccion in lista_transacciones:
        print(transaccion.obtener_informacion())

    print()

    print("Monto total:", calcular_monto_total(lista_transacciones))


# -------------------------------------------------------------
# INICIO DEL PROGRAMA
# -------------------------------------------------------------

ejecutar_sistema()