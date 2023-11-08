import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_automatizar_envio_info(self):
        driver=self.driver
        ruta_local=("file:///E:/Curso_Python_Selenium/Automatizacion_Selenium_Python/registro.html")

        driver.get(ruta_local)
        driver.maximize_window()
        time.sleep(3)
        campo_nombre=driver.find_element(By.NAME,"nombre")
        campo_nombre.send_keys("Ejemplo de Nombre")
        time.sleep(5)

        campo_email = driver.find_element(By.NAME, "email")
        campo_email.send_keys("armando@gmail.com")
        time.sleep(5)

        boton_enviar=driver.find_element(By.ID,"enviar")
        boton_enviar.click()

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
     unittest.main()
