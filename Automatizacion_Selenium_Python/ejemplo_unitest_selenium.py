import unittest
from selenium import webdriver
#todo clase que envia acciones por teclado
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_buscar(self):
        driver=self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google",driver.title)
        driver.maximize_window()
        elemento=driver.find_element(By.NAME,"q")
        elemento.send_keys("Selenium Documentacion",Keys.ARROW_DOWN)
        elemento.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "No se encontro el elemento" not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()




