import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_usando_Implicit_Wait(self):
        driver=self.driver
        driver.implicitly_wait(10)
        driver.get("http://ww.google.com")

        element=driver.find_element(By.NAME,"q")

if __name__=='__main__':
    unittest.main()

