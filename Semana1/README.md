# Actividad 2-1: Programación Orientada a Objetos

## Paso 1: Análisis de fragilidad

### Programación Estructurada

En la Semana 1 se desarrolló un programa utilizando Programación Estructurada (PE) para procesar transacciones de Quantum Core.

La información de cada transacción se almacenó en diccionarios con datos como `cliente_id`, `tipo` y `monto`. Por otra parte, las operaciones sobre estos datos se realizaron mediante funciones independientes como `calcular_monto_total()` y `filtrar_por_tipo()`.

### Problema al manejar diferentes tipos de transacciones

La Programación Estructurada funciona correctamente cuando el sistema es pequeño, pero puede volverse más difícil de mantener cuando aumenta la cantidad de tipos de transacciones.

Si Quantum Core necesitara manejar 10 tipos diferentes de transacciones, cada uno podría tener reglas y comportamientos diferentes. Por ejemplo, una transferencia podría tener una comisión, un retiro podría tener un límite y una devolución podría manejar reglas diferentes.

Si todas estas reglas se agregaran a las funciones existentes, estas podrían crecer demasiado y sería necesario modificar constantemente el código.

### Riesgo de debugging

Tener los datos separados de la lógica puede generar problemas durante el debugging porque las funciones dependen de que los datos tengan una estructura determinada.

Por ejemplo, la función `calcular_monto_total()` espera encontrar el campo `"monto"` dentro de cada transacción. Si ese dato cambia de nombre, cambia de tipo o tiene una estructura diferente, la función puede generar un error.

Además, cuando varias funciones trabajan sobre los mismos datos, puede ser más difícil identificar dónde se originó un problema.

### Necesidad de utilizar POO

La Programación Orientada a Objetos permite organizar los datos y los comportamientos relacionados dentro de una misma clase.

En este proyecto se puede crear una clase llamada `Transaccion`, que contenga los atributos `cliente_id`, `tipo` y `monto`, además de métodos relacionados con el comportamiento de una transacción.

De esta manera, los datos y las operaciones relacionadas quedan organizados dentro de un mismo objeto, facilitando el mantenimiento y crecimiento del programa.