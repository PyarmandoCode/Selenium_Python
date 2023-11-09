import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class usando_unitest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
    def test_cambiar_ventana(self):
        driver=self.driver
        # todo carga la pagina en la ventana 0
        driver.get("http://www.google.com")
        driver.maximize_window()
        time.sleep(3)
        driver.execute_script("window.open('');")#todo abre una nueva pestaña
        time.sleep(3)
        #todo carga la pagina en la ventana 1

        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        driver.maximize_window()
        time.sleep(3)

        # toogle=driver.find_element(By.XPATH,'//*[@id="main"]/label[3]/div')
        # toogle.click()
        # time.sleep(3)

        #todo abrir una nueva ventana 2
        driver.execute_script("window.open('');")  # todo abre una nueva pestaña
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[2])
        driver.get("https://www.w3schools.com/HOWTO/howto_custom_select.asp")
        #todo buscar el elemento select
        select=driver.find_element(By.XPATH,'//*[@id="main"]/div[3]/div[1]/select')
        #todo buscar sus opciones y recorrerlas dandole clik a c/u
        opciones=select.find_elements(By.TAG_NAME,"option")
        #lista_opciones=list()
        time.sleep(3)
        for option in opciones:
            option.click()
            #lista_opciones.append(option)
        #todo seleccionar la opcion indicada
        seleccionar=Select(driver.find_element(By.XPATH,'//*[@id="main"]/div[3]/div[1]/select'))
        seleccionar.select_by_value("10")
        time.sleep(3)
        # for item in lista_opciones:
        #     print(item.text)

        # todo carga la pagina en la ventana 0
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()


