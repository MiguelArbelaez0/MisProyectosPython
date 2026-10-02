import sqlite3
import os


# ============================================================
# 1. UBICACIÓN DE LA BASE DE DATOS
# ============================================================

ruta_db = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "quantum_wallet.db"
)


# ============================================================
# 2. CONEXIÓN CON SQLITE
# ============================================================

conexion = sqlite3.connect(ruta_db)
cursor = conexion.cursor()

# Activar llaves foráneas
cursor.execute("PRAGMA foreign_keys = ON")


# ============================================================
# 3. CREAR TABLA USUARIOS
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    nit TEXT
)
""")


# ============================================================
# 4. CREAR TABLA WALLETS
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS wallets (
    id_wallet INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo REAL DEFAULT 0.0,
    id_propietario INTEGER NOT NULL,
    FOREIGN KEY (id_propietario)
        REFERENCES usuarios(id_usuario)
)
""")


# ============================================================
# 5. DATOS DE PRUEBA
# ============================================================

usuarios_prueba = [
    (
        "MIGUEL ARBELAEZ VALLEJO",
        "miguel.arbelaez@example.com",
        "900000001-1",
        150000.50
    ),
    (
        "JOHANNES ANDRES BARRIOS RAVELES",
        "johannes.barrios@example.com",
        "900000002-2",
        250000.00
    ),
    (
        "JAVIER ANDRES BERROCAL ALVAREZ",
        "javier.berrocal@example.com",
        "900000003-3",
        480000.50
    ),
    (
        "JACOB MANUEL CAMACHO ACOSTA",
        "jacob.camacho@example.com",
        "900000004-4",
        125000.75
    ),
    (
        "DEIBIS ZULUAGA BAENA",
        "deibis.zuluaga@example.com",
        "900000005-5",
        750000.00
    ),
    (
        "DANIEL NAVARRO BELLO",
        "daniel.navarro@example.com",
        "900000006-6",
        320000.25
    ),
    (
        "JHON ALONSO PENARANDA REYES",
        "jhon.penaranda@example.com",
        "900000007-7",
        915000.00
    ),
    (
        "MARIA CRISTINA PINO LOPERA",
        "maria.pino@example.com",
        "900000008-8",
        180000.50
    ),
    (
        "JUANA IRIS RIOS MORELOS",
        "juana.rios@example.com",
        "900000009-9",
        560000.00
    ),
    (
        "ALEXANDER SILGADO BERRIO",
        "alexander.silgado@example.com",
        "900000010-0",
        430000.75
    )
]


# ============================================================
# 6. INSERTAR LOS 10 USUARIOS Y SUS WALLETS
# ============================================================

for nombre, email, nit, saldo in usuarios_prueba:

    cursor.execute("""
    INSERT INTO usuarios (nombre, email, nit)
    VALUES (?, ?, ?)
    """, (
        nombre,
        email,
        nit
    ))

    id_usuario = cursor.lastrowid

    cursor.execute("""
    INSERT INTO wallets (saldo, id_propietario)
    VALUES (?, ?)
    """, (
        saldo,
        id_usuario
    ))


# ============================================================
# 7. GUARDAR CAMBIOS
# ============================================================

conexion.commit()


# ============================================================
# 8. VERIFICAR RESULTADOS
# ============================================================

cursor.execute("SELECT COUNT(*) FROM usuarios")
total_usuarios = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM wallets")
total_wallets = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM usuarios u
LEFT JOIN wallets w
ON u.id_usuario = w.id_propietario
WHERE w.id_wallet IS NULL
""")

usuarios_sin_wallet = cursor.fetchone()[0]


# ============================================================
# 9. MOSTRAR RESULTADO
# ============================================================

print()
print("==============================================")
print("BASE DE DATOS CONFIGURADA CORRECTAMENTE")
print("==============================================")
print(f"Ubicación: {ruta_db}")
print(f"Total de usuarios: {total_usuarios}")
print(f"Total de wallets: {total_wallets}")
print(f"Usuarios sin wallet: {usuarios_sin_wallet}")
print("==============================================")


# ============================================================
# 10. CERRAR CONEXIÓN
# ============================================================

conexion.close()

print("Conexión cerrada.")