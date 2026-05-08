# Guía de Ejercicios SQlite

Hola, porfin me puse a trabajar :D, antes de entender como son estos ejercicios, recordemos estos conceptos básicos

- 1: Import sqlite3 (sqlite3 es una librería, solamente la estamos importando/llamando (de tu preferencia ese concepto) en el archivo)
- 2: sqlite.connect(archivos db) = esto lo que hace es conectar/crear tu archivo .db a python
2.1 Conectar: si le das la ruta correcta, solo le "conectas" el archivo a python
2.2 Crear: si no existe, lo crea en vsc (dependiendo de la ruta que des, lo crea dentro o fuera de la carpeta xd)
- 3: connect.cursor() y cursor.execute("query")
3.1 connect.cursor(): solamente llamas al cursor (que es necesario para que python ejecute diferentes consultas)
3.2 cursor.execute ("query"): en este amiguito de aquí, lo que hace es ejecutar diferentes consultas

# EJEMPLO DE CONSULTA: archivo northwind.db

-- """SELECT SUM(UnitsInStock) FROM Products WHERE Id = 1"""

aqui le pedimos que de la tabla products sume las unidadesenstock de el cual su id sea 1 

- 4: cursor.fetchall(): Devuelve todas las filas restantes
- 5: cursor.fetchone(): Devuelve solamente la fila encontrada
- 6: sqlite_master: este cabron es el puto padre, imaginate si fuera tu directorio principal:
lo que hace (segun tengo entendido) es que describe el esquema de cada tabla e incluye información adicional. 



# me tienen con las bolas por el piso tio msslkslkslkslskskls (no me busques)