# Importamos os para ubicar correctamente el archivo de transacciones
import os


# -------------------------------------------------------------
# FUNCIÓN 1: LECTURA Y ALMACENAMIENTO DE DATOS
# -------------------------------------------------------------

def leer_y_almacenar_datos(nombre_archivo):

    # Creamos una lista vacía para guardar las transacciones
    lista_transacciones = []

    # Abrimos el archivo en modo lectura
    with open(nombre_archivo, "r") as archivo:

        # Recorremos el archivo línea por línea
        for linea in archivo:

            # Quitamos espacios y saltos de línea
            # y dividimos los datos usando la coma
            partes = linea.strip().split(",")

            # Verificamos que la línea tenga 3 datos
            if len(partes) == 3:

                # Creamos un diccionario para representar
                # una transacción
                transaccion_dict = {
                    "cliente_id": partes[0].strip(),
                    "tipo": partes[1].strip(),
                    "monto": int(partes[2].strip())
                }

                # Agregamos el diccionario a la lista
                lista_transacciones.append(transaccion_dict)

    # Retornamos la lista de transacciones
    return lista_transacciones


# -------------------------------------------------------------
# FUNCIÓN 2: CÁLCULO DEL MONTO TOTAL
# -------------------------------------------------------------

def calcular_monto_total(lista_transacciones):

    # Comenzamos el total en cero
    total_monto = 0

    # Recorremos cada transacción
    for transaccion in lista_transacciones:

        # Sumamos el monto de cada transacción
        total_monto = total_monto + transaccion["monto"]

    # Retornamos el total
    return total_monto


# -------------------------------------------------------------
# FUNCIÓN 3: FILTRADO DE DATOS
# -------------------------------------------------------------

def filtrar_por_tipo(lista_transacciones, tipo_a_filtrar):

    # Creamos una lista vacía para guardar
    # las transacciones que coincidan
    lista_filtrada = []

    # Recorremos todas las transacciones
    for transaccion in lista_transacciones:

        # Comprobamos si el tipo coincide
        if transaccion["tipo"] == tipo_a_filtrar:

            # Si coincide, agregamos la transacción
            lista_filtrada.append(transaccion)

    # Retornamos la lista filtrada
    return lista_filtrada


# -------------------------------------------------------------
# FUNCIÓN PRINCIPAL DE EJECUCIÓN
# -------------------------------------------------------------

def ejecutar_sistema():

    # Obtenemos la carpeta donde está este archivo Python
    carpeta_actual = os.path.dirname(__file__)

    # Ubicamos el archivo transacciones.txt
    nombre_archivo = os.path.join(
        carpeta_actual,
        "transacciones.txt"
    )

    # Leemos y almacenamos las transacciones
    datos_cargados = leer_y_almacenar_datos(nombre_archivo)

    # Calculamos el monto total
    total = calcular_monto_total(datos_cargados)

    # Mostramos el monto total
    print("Monto total:", total)

    # Filtramos las transacciones de tipo CREDITO
    transacciones_credito = filtrar_por_tipo(
        datos_cargados,
        "CREDITO"
    )

    # Mostramos las transacciones filtradas
    print("Transacciones de tipo CREDITO:")
    print(transacciones_credito)


# -------------------------------------------------------------
# INICIO DEL PROGRAMA
# -------------------------------------------------------------

ejecutar_sistema()