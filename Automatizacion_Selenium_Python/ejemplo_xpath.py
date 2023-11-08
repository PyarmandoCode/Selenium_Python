import unittest
from selenium import webdriver
#todo clase que envia acciones por teclado
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_buscar_por_xpath(self):
        driver=self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        buscar_por_xpath=driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
        time.sleep(5)
        buscar_por_xpath.send_keys("Selenium",Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()