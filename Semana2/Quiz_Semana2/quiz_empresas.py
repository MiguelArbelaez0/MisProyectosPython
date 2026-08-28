# quiz_empresas.py


# 1) CLASE EMPRESA
class Empresa:

    def __init__(self, nombre, sector, num_empleados, ingresos_anuales):
        self.nombre = nombre
        self.sector = sector
        self.num_empleados = int(num_empleados)
        self.ingresos_anuales = int(ingresos_anuales)

    def obtener_informacion(self):
        return f"{self.nombre} | {self.sector} | {self.num_empleados} empleados | ${self.ingresos_anuales}"


# 2) LEER EL ARCHIVO Y CREAR OBJETOS
def leer_empresas(nombre_archivo):
    empresas = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, sector, num_empleados, ingresos_anuales = linea.strip().split(",")

            if int(num_empleados) > 0:
                empresa = Empresa(nombre, sector, num_empleados, ingresos_anuales)
                empresas.append(empresa)

    return empresas


# 3) SUMAR LOS INGRESOS
def calcular_total_ingresos(empresas):
    total = 0

    for empresa in empresas:
        total += empresa.ingresos_anuales

    return total


# 4) FILTRAR POR SECTOR
def filtrar_por_sector(empresas, sector):
    resultado = []

    for empresa in empresas:
        if empresa.sector == sector:
            resultado.append(empresa)

    return resultado


# 5) EMPRESA CON MÁS EMPLEADOS
def empresa_con_mas_empleados(empresas):
    if len(empresas) == 0:
        return None

    mayor = empresas[0]

    for empresa in empresas:
        if empresa.num_empleados > mayor.num_empleados:
            mayor = empresa

    return mayor


# 6) PROMEDIO DE EMPLEADOS
def promedio_empleados(empresas):
    if len(empresas) == 0:
        return 0

    total = 0

    for empresa in empresas:
        total += empresa.num_empleados

    return total / len(empresas)


# 7) FUNCIÓN PRINCIPAL
def ejecutar_quiz():
    empresas = leer_empresas("Semana2/Quiz_Semana2/empresas.txt")

    print("--- Empresas registradas ---")

    for empresa in empresas:
        print(empresa.obtener_informacion())

    print("\nTotal de ingresos:", calcular_total_ingresos(empresas))

    print("\n--- Empresas del sector TECNOLOGIA ---")

    for empresa in filtrar_por_sector(empresas, "TECNOLOGIA"):
        print(empresa.obtener_informacion())

    mejor = empresa_con_mas_empleados(empresas)

    if mejor is not None:
        print("\nEmpresa con mas empleados:", mejor.obtener_informacion())

    print("\nPromedio de empleados:", promedio_empleados(empresas))


# Iniciar el programa
ejecutar_quiz()

