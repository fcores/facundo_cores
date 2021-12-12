import sqlite3

miconexcion=sqlite3.connect(r"C:\Users\facucores\Desktop\bbdd\bbdd_cores")

micursor=miconexcion.cursor()

micursor.execute("SELECT * FROM PRODUCTOS") ##Genero una consulta

muchosproductos=micursor.fetchall() ##Me guardo la conulta en una lista

for i in muchosproductos:
    print("Nombre: ", i[0], " Precio: ",i[1])

#micursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50), PRECIO INTEGER,SECCION VARCHAR(20))") ##Crea las tablas
#micursor.execute("INSERT INTO PRODUCTOS VALUES('CAMISETA',25,'MODA')") ##Inserta un dato
#muchosproductos=[("Patin",100,"Deportes"),("Cenicero",20,"Ceramica"),("Pantalon",80,"Moda")] ##Genero una lista para agregarla a la tabla
#micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",muchosproductos) ##Agrego muchos datos
#miconexcion.commit() ##Ejecutar el ingreso de informacion

micursor.close()

miconexcion.close()


