# -------------------------------------------------------------
# ACTIVIDAD 2-1: PROGRAMACION ORIENTADA A OBJETOS
# Quantum Core
# -------------------------------------------------------------


# -------------------------------------------------------------
# CLASE TRANSACCION
# -------------------------------------------------------------

class Transaccion:

    # Constructor de la clase
    # Recibe los datos de una transacción
    def __init__(self, cliente_id, tipo, monto):

        # Guardamos los datos como atributos del objeto
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    # Método para obtener la información de una transacción
    def obtener_informacion(self):

        return (
            f"Cliente: {self.cliente_id}, "
            f"Tipo: {self.tipo}, "
            f"Monto: {self.monto}"
        )


# -------------------------------------------------------------
# FUNCIÓN PARA LEER Y CREAR OBJETOS TRANSACCION
# -------------------------------------------------------------

def leer_y_almacenar_datos(nombre_archivo):

    # Creamos una lista vacía para almacenar
    # los objetos Transaccion
    lista_transacciones = []

    # Abrimos el archivo en modo lectura
    with open(nombre_archivo, "r") as archivo:

        # Recorremos el archivo línea por línea
        for linea in archivo:

            # Quitamos espacios y dividimos la línea
            # usando la coma como separador
            partes = linea.strip().split(",")

            # Verificamos que existan tres datos
            if len(partes) == 3:

                # Creamos un objeto de la clase Transaccion
                transaccion = Transaccion(
                    partes[0].strip(),
                    partes[1].strip(),
                    int(partes[2].strip())
                )

                # Guardamos el objeto dentro de la lista
                lista_transacciones.append(transaccion)

    # Retornamos la lista de objetos
    return lista_transacciones


# -------------------------------------------------------------
# FUNCIÓN PARA CALCULAR EL MONTO TOTAL
# -------------------------------------------------------------

def calcular_monto_total(lista_transacciones):

    # Comenzamos el total en cero
    total_monto = 0

    # Recorremos la lista de objetos
    for transaccion in lista_transacciones:

        # Sumamos el atributo monto de cada objeto
        total_monto = total_monto + transaccion.monto

    # Retornamos el total
    return total_monto


# -------------------------------------------------------------
# FUNCIÓN PARA FILTRAR POR TIPO
# -------------------------------------------------------------

def filtrar_por_tipo(lista_transacciones, tipo_a_filtrar):

    # Creamos una nueva lista para guardar
    # los objetos que coincidan
    lista_filtrada = []

    # Recorremos todos los objetos
    for transaccion in lista_transacciones:

        # Comprobamos el tipo de cada objeto
        if transaccion.tipo == tipo_a_filtrar:

            # Agregamos el objeto a la nueva lista
            lista_filtrada.append(transaccion)

    # Retornamos la lista filtrada
    return lista_filtrada


# -------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# -------------------------------------------------------------

def ejecutar_sistema():

    # Obtenemos la carpeta donde está este archivo
    carpeta_actual = os.path.dirname(__file__)

    # Ubicamos el archivo de transacciones
    nombre_archivo = os.path.join(
        carpeta_actual,
        "transacciones.txt"
    )

    # Leemos el archivo y creamos una lista de objetos
    lista_transacciones = leer_y_almacenar_datos(nombre_archivo)

    # Calculamos el monto total
    total = calcular_monto_total(lista_transacciones)

    # Mostramos el total
    print("Monto total:", total)

    # Filtramos las transacciones de tipo CREDITO
    transacciones_credito = filtrar_por_tipo(
        lista_transacciones,
        "CREDITO"
    )

    # Mostramos las transacciones filtradas
    print("\nTransacciones de tipo CREDITO:")

    for transaccion in transacciones_credito:
        print(transaccion.obtener_informacion())


# -------------------------------------------------------------
# IMPORTAMOS OS PARA TRABAJAR CON LA RUTA DEL ARCHIVO
# -------------------------------------------------------------

import os


# -------------------------------------------------------------
# INICIO DEL PROGRAMA
# -------------------------------------------------------------

ejecutar_sistema()