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
# 2. CONEXIÓN CON LA BASE DE DATOS
# ============================================================

conexion = sqlite3.connect(ruta_db)

cursor = conexion.cursor()

# Activar llaves foráneas
cursor.execute("PRAGMA foreign_keys = ON")


# ============================================================
# 3. CREAR TABLA CONTACTOS
# ============================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS contactos (
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apodo TEXT NOT NULL,
    id_propietario INTEGER NOT NULL,
    FOREIGN KEY (id_propietario)
        REFERENCES usuarios(id_usuario)
)
""")


# ============================================================
# 4. CREATE - INSERTAR 5 CONTACTOS
# ============================================================

contactos = [
    ("Mateo Aguilar", "Mateo", 1),
    ("Sara Quintero", "Sari", 1),
    ("Carlos Dev", "Carlitos", 1),
    ("Laura Gómez", "Lau", 1),
    ("Andrés Torres", "Andy", 1)
]

for nombre, apodo, propietario in contactos:

    cursor.execute("""
    INSERT INTO contactos (
        nombre,
        apodo,
        id_propietario
    )
    VALUES (?, ?, ?)
    """, (
        nombre,
        apodo,
        propietario
    ))

print("CREATE: 5 contactos insertados correctamente.")


# ============================================================
# 5. READ - CONSULTAR CONTACTOS DEL USUARIO 1
# ============================================================

cursor.execute("""
SELECT id_contacto, nombre, apodo, id_propietario
FROM contactos
WHERE id_propietario = ?
ORDER BY id_contacto
""", (1,))

contactos_usuario = cursor.fetchall()


print()
print("READ: Contactos del usuario 1")
print("-" * 60)

for contacto in contactos_usuario:
    print(
        f"ID: {contacto[0]} | "
        f"Nombre: {contacto[1]} | "
        f"Apodo: {contacto[2]} | "
        f"Propietario: {contacto[3]}"
    )


# ============================================================
# 6. UPDATE - CAMBIAR EL APODO DEL CONTACTO 2
# ============================================================

cursor.execute("""
UPDATE contactos
SET apodo = ?
WHERE id_contacto = ?
""", (
    "Sara QA",
    2
))

print()
print("UPDATE: Apodo del contacto 2 actualizado correctamente.")


# ============================================================
# 7. VERIFICAR EL UPDATE
# ============================================================

cursor.execute("""
SELECT id_contacto, nombre, apodo, id_propietario
FROM contactos
WHERE id_contacto = ?
""", (2,))

contacto_actualizado = cursor.fetchone()

if contacto_actualizado:
    print(
        f"Contacto actualizado → "
        f"ID: {contacto_actualizado[0]} | "
        f"Nombre: {contacto_actualizado[1]} | "
        f"Apodo: {contacto_actualizado[2]} | "
        f"Propietario: {contacto_actualizado[3]}"
    )


# ============================================================
# 8. DELETE - ELIMINAR CONTACTO CON ID 2
# ============================================================

cursor.execute("""
DELETE FROM contactos
WHERE id_contacto = ?
""", (2,))

print()
print("DELETE: Contacto con ID 2 eliminado correctamente.")


# ============================================================
# 9. GUARDAR CAMBIOS
# ============================================================

conexion.commit()


# ============================================================
# 10. MOSTRAR ESTADO FINAL
# ============================================================

cursor.execute("""
SELECT id_contacto, nombre, apodo, id_propietario
FROM contactos
WHERE id_propietario = ?
ORDER BY id_contacto
""", (1,))

contactos_finales = cursor.fetchall()


print()
print("ESTADO FINAL DE CONTACTOS DEL USUARIO 1")
print("-" * 60)

for contacto in contactos_finales:
    print(
        f"ID: {contacto[0]} | "
        f"Nombre: {contacto[1]} | "
        f"Apodo: {contacto[2]} | "
        f"Propietario: {contacto[3]}"
    )


# ============================================================
# 11. CONTAR CONTACTOS
# ============================================================

cursor.execute("""
SELECT COUNT(*)
FROM contactos
WHERE id_propietario = ?
""", (1,))

total_contactos = cursor.fetchone()[0]

print()
print(f"Total de contactos del usuario 1: {total_contactos}")


# ============================================================
# 12. CERRAR CONEXIÓN
# ============================================================

conexion.close()

print("Conexión cerrada.")