import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#todo es una tecnica conocica como espera explicita("explicit wait)
#todo en la que el codigo espera un tiempo especifico hasta que se cumpla
#todo una determinada condicion antest de continuar con la ejecucion del script

class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_usando_Explict_Wait(self):
        driver=self.driver
        driver.get("http://www.google.com")
        try:
            element=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.NAME,"q"))
            )
            element.send_keys("Selenium")
            element.send_keys(Keys.RETURN)
        finally:
            driver.quit()

    def test_mi_nueva_pagina(self):
        driver=self.driver
        driver.get("http://www.mipagina.com")
        try:
            element=WebDriverWait(driver,10).until(
                EC.visibility_of_element_located((By.ID,"mielemento"))
            )
            element.click()

        finally:
            driver.close()

if __name__=='__main__':
    unittest.main()
