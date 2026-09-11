# ============================================================
# FUNDAMENTOS DE SOFTWARE
# Actividad 4-2: Serialización y persistencia (JSON)
# Semana 4
# Autor: Miguel Arbeláez
#
# Objetivo:
# Demostrar el proceso de serialización y deserialización
# de un objeto TransaccionCredito utilizando JSON.
# ============================================================

import json


# Clase utilizada para representar una transacción
class TransaccionCredito:

    def __init__(self, cliente_id, tipo, monto):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    # Permite mostrar la información del objeto
    def __str__(self):
        return (
            f"Transacción [{self.tipo}] - "
            f"ID: {self.cliente_id}, "
            f"Monto: {self.monto}"
        )


# Convierte un objeto TransaccionCredito en un diccionario
def objeto_a_diccionario(transaccion):

    datos = {
        "cliente_id": transaccion.cliente_id,
        "tipo": transaccion.tipo,
        "monto": transaccion.monto
    }

    return datos


# Convierte un diccionario en una cadena JSON
def diccionario_a_json(datos):

    texto_json = json.dumps(datos)

    return texto_json


# Convierte una cadena JSON en un diccionario
def json_a_diccionario(texto_json):

    datos = json.loads(texto_json)

    return datos


# Convierte un diccionario nuevamente en un objeto
def diccionario_a_objeto(datos):

    transaccion = TransaccionCredito(
        datos["cliente_id"],
        datos["tipo"],
        datos["monto"]
    )

    return transaccion


# Función principal para demostrar el proceso
def ejecutar():

    # --------------------------------------------------------
    # 1. OBJETO ORIGINAL
    # --------------------------------------------------------

    original = TransaccionCredito(
        "C002",
        "CREDITO",
        500000
    )

    print("1) Objeto original:")
    print(original)

    print("Tipo de dato:", type(original).__name__)
    print("")


    # --------------------------------------------------------
    # 2. SERIALIZACIÓN
    # Objeto -> Diccionario -> JSON
    # --------------------------------------------------------

    datos = objeto_a_diccionario(original)

    print("2) Diccionario:")
    print(datos)
    print("Tipo de dato:", type(datos).__name__)
    print("")

    texto_json = diccionario_a_json(datos)

    print("3) Serializado:")
    print(texto_json)
    print("Tipo de dato:", type(texto_json).__name__)
    print("")


    # --------------------------------------------------------
    # 3. DESERIALIZACIÓN
    # JSON -> Diccionario -> Objeto
    # --------------------------------------------------------

    datos_recuperados = json_a_diccionario(texto_json)

    print("4) Diccionario recuperado:")
    print(datos_recuperados)
    print("Tipo de dato:", type(datos_recuperados).__name__)
    print("")

    reconstruido = diccionario_a_objeto(datos_recuperados)

    print("5) Objeto deserializado:")
    print(reconstruido)
    print("Tipo de dato:", type(reconstruido).__name__)


# Ejecuta la demostración
if __name__ == "__main__":
    ejecutar()