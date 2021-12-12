import sqlite3

miconexcion=sqlite3.connect(r"C:\Users\facucores\Desktop\bbdd\GestionPedidos2")

micursor=miconexcion.cursor()


# micursor.execute('''
#     CREATE TABLE OTROSPRODUCTOS (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARCHAR(40),
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
#     )''')

# miproductos=[
    
#     ("camiseta",35,"Moda"),
#     ("pantalon",35,"Juguete"),
#     ("coche",35,"Pelotas"),
#     ("gorra",35,"Perros"),
#     ("zapatilla",35,"Gatos"),
#     ("remera",35,"Moda")
#     ]

# micursor.execute("INSERT INTO PRODUCTOS VALUES('AR07','ZAPATOS','90','DEPORTES')") "Agregar datos de forma individual"

# micursor.executemany("INSERT INTO OTROSPRODUCTOS VALUES (NULL,?,?,?)",miproductos) ##Agregar varios datos

#micursor.execute("UPDATE OTROSPRODUCTOS SET PRECIO=50 WHERE ID=2") ## actualiar datoss

micursor.execute("DELETE FROM OTROSPRODUCTOS WHERE ID=2") ## Borrar una fila de la base de datos

miconexcion.commit() ##Ejecutar el ingreso de informacion


micursor.close()

miconexcion.close()