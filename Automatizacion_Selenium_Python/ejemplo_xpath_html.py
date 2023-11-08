import unittest
from selenium import webdriver
#todo clase que envia acciones por teclado
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_buscar_elementos_Dom(self):
        driver=self.driver
        driver.get("file:///E:/Curso_Python_Selenium/Automatizacion_Selenium_Python/index.html")
        time.sleep(3)
        titulo=driver.find_element(By.XPATH,"//h1")
        parrafo = driver.find_element(By.XPATH, "//p")
        componente_ul= driver.find_element(By.XPATH, '//*[@id="mi_lista"]')
        componente_lista=componente_ul.find_elements(By.TAG_NAME,"li")
        mi_lista=list()
        for elementos in componente_lista:
            mi_lista.append(elementos)

        #todo imprimir el texto seleccionado
        print(f"Titulo {titulo.text}")
        print(f"Parrafo {parrafo.text}")

        for elementos in mi_lista:
            print(elementos.text)

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()