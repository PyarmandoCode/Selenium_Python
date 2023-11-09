#todo permitir persister los datos de mi Automatizacion
import sqlite3

class MiBaseDeDatos:
    def __init__(self,nombre_archivo):
        self.conexion=sqlite3.connect(nombre_archivo)
        self.cursor =self.conexion.cursor()
        self.crear_tabla()


    def cerrar_conexion(self):
        self.conexion.close()
        print("Conexion Cerrada")

    def crear_tabla(self):
        consulta = '''
        CREATE TABLE IF NOT EXISTS productos(
            codigo INTEGER PRIMARY KEY,
            nombre TEXT,
            precio INTEGER
        )
        '''
        self.cursor.execute(consulta)
        self.conexion.commit()

    def insertar_registros(self,nombre,precio):
        consulta= 'INSERT INTO productos (nombre,precio)Values (?,?)'
        valores = (nombre,precio)
        self.cursor.execute(consulta,valores)
        self.conexion.commit()

    def consultar_registros(self):
        consulta='SELECT * FROM productos'
        self.cursor.execute(consulta)
        resultados=self.cursor.fetchall()
        return resultados


#Crear una Instancia de la clase MiBaseDeDatos
mi_db = MiBaseDeDatos('automatizacion.db')
# mi_db.insertar_registros('PRODUCTO XYZ',200)
# mi_db.insertar_registros('PRODUCTO MYZ',300)
# mi_db.insertar_registros('PRODUCTO LYZ',400)
# mi_db.insertar_registros('PRODUCTO PYZ',500)
# mi_db.insertar_registros('PRODUCTO TYZ',600)
# mi_db.insertar_registros('PRODUCTO LYZ',200)

resultados=mi_db.consultar_registros()
for resultado in resultados:
    print(resultado)
mi_db.cerrar_conexion()

