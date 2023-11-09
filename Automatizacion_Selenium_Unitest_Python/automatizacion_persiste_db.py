import time
import unittest
import sqlite3
from selenium import webdriver

class usando_unitest(unittest.TestCase):
    def setUp(self): #todo se debe llamar asi SetUp
        self.driver = webdriver.Chrome()
    def test_automatizar_bd(self):
        driver = self.driver
        driver.get("http://www.gmail.com")
        time.sleep(3)
        username = "aruiz"
        resultado = "success-ok"
        self.save_result_to_database(username,resultado)
    def save_result_to_database(self,username,result):
        conn=sqlite3.connect('resultados.db')
        cursor=conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultado (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT,
             result TEXT
            )
        ''')
        #TODO INSERTAR EL RESULTADO DE LA PRUEBA EN LA BD
        cursor.execute("INSERT INTO resultado(username,result) VALUES (?,?)",(username,result))
        #todo GUARDAR LOS CAMBIOS Y CERRAR LA CONEXION
        conn.commit()
        conn.close()

    # def tearDown(self):
    #     self.driver.close()
if __name__=='__main__':
    unittest.main()

