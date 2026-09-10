# ============================================================
# FUNDAMENTOS DE SOFTWARE
# Actividad 4-1: Implementación de la recuperación try-except
# Semana 4
# Autor: Miguel Arbeláez
#
# Objetivo:
# Implementar el manejo de excepciones mediante try-except
# para detectar errores en los datos, informar el problema y
# continuar procesando las transacciones válidas.
# ============================================================

import os


# Clase base para representar una transaccion
class TransaccionBase:
    def __init__(self, cliente_id, tipo, monto):
        self._cliente_id = cliente_id
        self._tipo = tipo
        self._monto = 0

        # Se utiliza el setter para validar el monto
        self.monto = monto

    # Getter para obtener el ID del cliente
    @property
    def cliente_id(self):
        return self._cliente_id

    # Getter para obtener el tipo de transaccion
    @property
    def tipo(self):
        return self._tipo

    # Getter para obtener el monto
    @property
    def monto(self):
        return self._monto

    # Setter para validar el monto de la transaccion
    @monto.setter
    def monto(self, nuevo_monto):
        # No se permiten montos negativos
        if nuevo_monto < 0:
            raise ValueError("El monto no puede ser negativo.")

        self._monto = nuevo_monto

    # Devuelve la informacion de la transaccion
    def obtener_informacion(self):
        return (
            f"Cliente: {self.cliente_id}, "
            f"Tipo: {self.tipo}, "
            f"Monto: {self.monto}"
        )


# Clase para las transacciones de credito
class TransaccionCredito(TransaccionBase):
    pass


# Clase para las transacciones de debito
class TransaccionDebito(TransaccionBase):
    pass


# Funcion encargada de leer y almacenar las transacciones
def leer_y_almacenar_datos(nombre_archivo):
    lista_transacciones = []

    # Se abre el archivo utilizando with
    with open(nombre_archivo, "r") as archivo:
        numero_linea = 0

        # Se recorren todas las lineas del archivo
        for linea in archivo:
            numero_linea += 1

            # Se separan los datos utilizando la coma
            partes = linea.strip().split(",")

            try:
                # Se verifica que la linea tenga los tres datos necesarios
                if len(partes) != 3:
                    raise TypeError(
                        "La transaccion no tiene los 3 datos requeridos."
                    )

                # Se obtienen los datos de la transaccion
                cliente_id = partes[0].strip()
                tipo = partes[1].strip()

                # Se convierte el monto de texto a entero
                monto = int(partes[2].strip())

                # Se crea el objeto dependiendo del tipo de transaccion
                if tipo == "CREDITO":
                    transaccion = TransaccionCredito(
                        cliente_id, tipo, monto
                    )

                elif tipo == "DEBITO":
                    transaccion = TransaccionDebito(
                        cliente_id, tipo, monto
                    )

                else:
                    # Se genera un error si el tipo no es reconocido
                    raise ValueError("Tipo de transaccion desconocido.")

                # Si no hubo errores, se agrega a la lista
                lista_transacciones.append(transaccion)

            # Captura errores relacionados con valores incorrectos
            except ValueError as error:
                print(
                    f"[ERROR ValueError] Linea {numero_linea}: "
                    f"{linea.strip()} -> {error}"
                )

            # Captura errores relacionados con datos insuficientes
            except TypeError as error:
                print(
                    f"[ERROR TypeError] Linea {numero_linea}: "
                    f"{linea.strip()} -> {error}"
                )

    # Se devuelve la lista con las transacciones validas
    return lista_transacciones


# Funcion principal del programa
def ejecutar_sistema():
    # Obtiene la carpeta donde se encuentra este archivo
    carpeta_actual = os.path.dirname(__file__)

    # Construye la ruta del archivo de transacciones
    nombre_archivo = os.path.join(
        carpeta_actual,
        "transacciones_corruptas.txt"
    )

    # Lee las transacciones y maneja los errores encontrados
    transacciones = leer_y_almacenar_datos(nombre_archivo)

    print("\n--- TRANSACCIONES VALIDAS ---")

    # Muestra las transacciones que fueron procesadas correctamente
    for transaccion in transacciones:
        print(transaccion.obtener_informacion())

    # Muestra la cantidad total de transacciones validas
    print("\nTotal de transacciones validas:", len(transacciones))


# Inicia la ejecucion del sistema
ejecutar_sistema()