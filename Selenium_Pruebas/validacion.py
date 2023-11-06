#todo importando la libreria de selenium
from selenium import webdriver
import time
#todo crear el objeto driver de Chrome
driver = webdriver.Chrome()
#todo automatizando la web de Python
driver.get("http://python.org")
driver.maximize_window()
#todo indicas el tiempo de espera
time.sleep(7)
#todo cerrando el driver
driver.close()
