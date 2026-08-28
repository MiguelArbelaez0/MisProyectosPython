# -------------------------------------------------------------
# ACTIVIDAD 2-1: PROGRAMACIÓN ORIENTADA A OBJETOS
# Quantum Core
# -------------------------------------------------------------

import os


# -------------------------------------------------------------
# CLASE TRANSACCION
# -------------------------------------------------------------

class Transaccion:

    # Constructor de la clase
    def __init__(self, cliente_id, tipo, monto):

        # Atributos del objeto
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    # Método para obtener la información de la transacción
    def obtener_informacion(self):

        return (
            f"Cliente: {self.cliente_id}, "
            f"Tipo: {self.tipo}, "
            f"Monto: {self.monto}"
        )


# -------------------------------------------------------------
# FUNCIÓN PARA LEER Y ALMACENAR LOS DATOS
# -------------------------------------------------------------

def leer_y_almacenar_datos(nombre_archivo):

    # Lista que almacenará los objetos Transaccion
    lista_transacciones = []

    # Abrimos el archivo en modo lectura
    with open(nombre_archivo, "r") as archivo:

        # Recorremos cada línea del archivo
        for linea in archivo:

            # Quitamos espacios y dividimos la línea por comas
            partes = linea.strip().split(",")

            # Verificamos que la línea tenga tres datos
            if len(partes) == 3:

                # Creamos un objeto Transaccion
                transaccion = Transaccion(
                    partes[0].strip(),
                    partes[1].strip(),
                    int(partes[2].strip())
                )

                # Agregamos el objeto a la lista
                lista_transacciones.append(transaccion)

    # Retornamos la lista de objetos
    return lista_transacciones


# -------------------------------------------------------------
# FUNCIÓN PARA CALCULAR EL MONTO TOTAL
# -------------------------------------------------------------

def calcular_monto_total(lista_transacciones):

    # Iniciamos el total en cero
    total_monto = 0

    # Recorremos la lista de objetos
    for transaccion in lista_transacciones:

        # Sumamos el monto de cada objeto
        total_monto = total_monto + transaccion.monto

    # Retornamos el resultado
    return total_monto


# -------------------------------------------------------------
# FUNCIÓN PARA FILTRAR POR TIPO
# -------------------------------------------------------------

def filtrar_por_tipo(lista_transacciones, tipo_a_filtrar):

    # Creamos una lista para las transacciones filtradas
    lista_filtrada = []

    # Recorremos todos los objetos
    for transaccion in lista_transacciones:

        # Comprobamos si el tipo coincide
        if transaccion.tipo == tipo_a_filtrar:

            # Agregamos el objeto a la lista filtrada
            lista_filtrada.append(transaccion)

    # Retornamos la lista filtrada
    return lista_filtrada


# -------------------------------------------------------------
# FUNCIÓN PRINCIPAL DE EJECUCIÓN
# -------------------------------------------------------------

def ejecutar_sistema():

    # Obtenemos la carpeta donde está este archivo
    carpeta_actual = os.path.dirname(__file__)

    # Creamos la ruta completa del archivo de transacciones
    nombre_archivo = os.path.join(
        carpeta_actual,
        "transacciones.txt"
    )

    # Leemos el archivo y creamos los objetos
    lista_transacciones = leer_y_almacenar_datos(nombre_archivo)

    # Calculamos el monto total
    total = calcular_monto_total(lista_transacciones)

    # Mostramos el monto total
    print("Monto total:", total)

    # Filtramos las transacciones de tipo CREDITO
    transacciones_credito = filtrar_por_tipo(
        lista_transacciones,
        "CREDITO"
    )

    # Mostramos las transacciones filtradas
    print()
    print("Transacciones de tipo CREDITO:")

    # Mostramos cada objeto de la lista filtrada
    for transaccion in transacciones_credito:
        print(transaccion.obtener_informacion())


# -------------------------------------------------------------
# INICIO DEL PROGRAMA
# -------------------------------------------------------------

ejecutar_sistema()