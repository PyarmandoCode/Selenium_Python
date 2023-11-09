import unittest
from selenium import webdriver
import time


class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_pagina_siguinte_o_anterior(self):
        driver=self.driver
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.python.org")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
    def tearDown(self):
        self.driver.close()
if __name__=='__main__':
    unittest.main()


