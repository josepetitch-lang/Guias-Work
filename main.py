import sqlite3

# Conceptos Clave:

# connect() = permite obtener la conexión
# cursor() = crea un objeto cursor que permite ejecutar 
# cursor.execute() = ejecuta sentencias sql
# commit() = guarda los cambios realizados en la base 
# close() = cierra la conexión a la base de datos
# fetchall() = recupera todas las filas de la ultima consulta SELECT
# fetchone() = recupera la siguiente fila xd


# cursor.execute ("SELECT * FROM PRODUCTOS")
# cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Ana', 30)")

#sqlite y python son novios


connection = sqlite3.connect("molleja.db")

cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS USUARIOS 
               ( id INTEGER PRIMARY KEY,
                 name TEXT,
                 descrip INTEGER
                      
               )
               """)

cursor.execute("INSERT INTO usuarios VALUES (101, 'Viktor Miquilena', 'Administrador')")
cursor.execute("INSERT INTO usuarios VALUES (102, 'Eliana Chirinos', 'Ingeniera Civil')")
cursor.execute("INSERT INTO usuarios VALUES (103, 'Andrea Petit', 'Papu Pro')")
print("Usuarios ingresados correctamente")

connection.commit()
connection.close()


