import sqlite3

# 1. Conectar con la base de datos
conexion = sqlite3.connect("quantum_wallet.db")

# 2. Crear el cursor
cursor = conexion.cursor()

# 3. Activar las llaves foráneas
cursor.execute("PRAGMA foreign_keys = ON")

# 4. Crear la tabla usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    nit TEXT
)
""")

# 5. Crear la tabla wallets
cursor.execute("""
CREATE TABLE IF NOT EXISTS wallets (
    id_wallet INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo REAL DEFAULT 0.0,
    id_propietario INTEGER NOT NULL,
    FOREIGN KEY (id_propietario)
        REFERENCES usuarios(id_usuario)
)
""")

# 6. Insertar un usuario de prueba
try:
    cursor.execute("""
    INSERT INTO usuarios (nombre, email, nit)
    VALUES (?, ?, ?)
    """, (
        "Juan Perez",
        "juan@mail.com",
        "900123456-1"
    ))

    conexion.commit()
    print("Usuario insertado correctamente.")

except sqlite3.IntegrityError:
    print("El usuario ya existe.")

# 7. Obtener el ID del usuario
cursor.execute("""
SELECT id_usuario
FROM usuarios
WHERE email = ?
""", ("juan@mail.com",))

usuario = cursor.fetchone()

# 8. Insertar una wallet relacionada con el usuario
if usuario:
    id_usuario = usuario[0]

    # Verificar si ya existe una wallet para este usuario
    cursor.execute("""
    SELECT id_wallet
    FROM wallets
    WHERE id_propietario = ?
    """, (id_usuario,))

    wallet = cursor.fetchone()

    if wallet:
        print("La wallet ya existe.")
    else:
        cursor.execute("""
        INSERT INTO wallets (saldo, id_propietario)
        VALUES (?, ?)
        """, (
            150000.50,
            id_usuario
        ))

        conexion.commit()
        print("Wallet insertada correctamente.")

# 9. Mostrar mensaje de confirmación
print("Base de datos configurada correctamente.")

# 10. Cerrar la conexión
conexion.close()

print("Conexión cerrada.")